#!/usr/bin/env python3
"""Fotos fürs Web aufbereiten: verkleinern, Wasserzeichen, Urheber-Metadaten, Manifest.

Ablauf pro Foto in «Webseite - Bilder/<kategorie>/»:
  1. Prüfen, ob der Export aus Lightroom Urheber und Copyright enthält. Fehlt etwas,
     wird das Foto nicht verarbeitet.
  2. In mehreren Breiten als WebP speichern (für srcset), jeweils mit Wasserzeichen.
  3. Urheber, Copyright und Bildbeschreibung in jede WebP-Datei schreiben. Alles andere
     (GPS, Seriennummer der Kamera) fällt weg.
  4. Eintrag in data/fotos.json schreiben, die Galerie liest daraus.

Aufruf im Projektordner:
  python3 tools/bilder.py            neue und geänderte Fotos verarbeiten
  python3 tools/bilder.py --alle     alle Fotos neu rechnen (z. B. nach neuem Wasserzeichen)
  python3 tools/bilder.py --pruefen  nur prüfen, ob alle Web-Fotos die Urheber-Metadaten tragen

Braucht: Pillow (pip3 install Pillow) und exiftool (brew install exiftool).
"""

import argparse
import json
import re
import subprocess
import sys
import unicodedata
from io import BytesIO
from pathlib import Path

from PIL import Image, ImageCms, ImageDraw, ImageFont, ImageOps

PROJEKT = Path(__file__).resolve().parent.parent

# ---------- Einstellungen ----------

URHEBER = "Yannic Doutaz"
WEBSEITE = "https://yannicdoutaz.github.io/portfolio-page/"
WASSERZEICHEN = f"© {URHEBER}"

EINGANG = PROJEKT / "Webseite - Bilder"      # Lightroom-Exporte, nicht im Repo
AUSGANG = PROJEKT / "assets" / "img" / "fotos"
MANIFEST = PROJEKT / "data" / "fotos.json"

BREITEN = (640, 1280, 1920, 2560)  # 2560 nur für die Grossansicht auf grossen Bildschirmen
QUALITAET = 80                     # WebP-Qualität, ab ca. 80 sieht man keinen Unterschied mehr
ENDUNGEN = {".jpg", ".jpeg", ".png", ".tif", ".tiff"}
SCHRIFT = "/System/Library/Fonts/Avenir Next.ttc"


# ---------- Metadaten (exiftool) ----------

def lies_metadaten(dateien):
    """Liest Urheber-, Copyright- und Beschreibungsfelder aller Dateien in einem Durchgang."""
    if not dateien:
        return {}
    befehl = [
        "exiftool", "-json", "-charset", "utf8",
        "-XMP-dc:Creator", "-EXIF:Artist", "-IPTC:By-line",
        "-XMP-dc:Rights", "-EXIF:Copyright", "-IPTC:CopyrightNotice",
        "-XMP-dc:Description", "-IPTC:Caption-Abstract", "-XMP-dc:Title",
        *map(str, dateien),
    ]
    ausgabe = subprocess.run(befehl, capture_output=True, text=True, check=False).stdout
    return {Path(eintrag["SourceFile"]).resolve(): eintrag for eintrag in json.loads(ausgabe or "[]")}


def als_text(wert):
    """exiftool liefert Listenfelder (z. B. mehrere Urheber) als Liste."""
    if isinstance(wert, list):
        return ", ".join(map(str, wert))
    return str(wert or "")


def fehlende_rechte(meta):
    """Gibt zurück, was fehlt. Leere Liste heisst: Urheber und Copyright sind vorhanden."""
    urheber = " ".join(als_text(meta.get(f)) for f in ("Creator", "Artist", "By-line"))
    rechte = " ".join(als_text(meta.get(f)) for f in ("Rights", "Copyright", "CopyrightNotice"))
    fehlt = []
    if URHEBER not in urheber:
        fehlt.append("Urheber")
    if URHEBER not in rechte:
        fehlt.append("Copyright")
    return fehlt


def schreibe_rechte(quelle, ziele):
    """Übernimmt Urheber, Copyright und Beschreibung aus dem Export in die Web-Dateien."""
    befehl = [
        "exiftool", "-overwrite_original", "-q", "-charset", "utf8",
        "-tagsFromFile", str(quelle),
        "-XMP-dc:Creator<XMP-dc:Creator", "-XMP-dc:Rights<XMP-dc:Rights",
        "-XMP-dc:Description<XMP-dc:Description", "-XMP-dc:Title<XMP-dc:Title",
        "-EXIF:Artist<EXIF:Artist", "-EXIF:Copyright<EXIF:Copyright",
        # Fixe Angaben: Bild ist urheberrechtlich geschützt, mehr dazu auf der Webseite
        "-XMP-xmpRights:Marked=True", f"-XMP-xmpRights:WebStatement={WEBSEITE}",
        *map(str, ziele),
    ]
    subprocess.run(befehl, check=True)


# ---------- Bild ----------

def nach_srgb(bild):
    """Browser zeigen sRGB. Andere Farbprofile (z. B. Adobe RGB) werden umgerechnet."""
    profil = bild.info.get("icc_profile")
    if profil:
        quelle = ImageCms.ImageCmsProfile(BytesIO(profil))
        ziel = ImageCms.createProfile("sRGB")
        bild = ImageCms.profileToProfile(bild, quelle, ziel, outputMode="RGB")
    return bild.convert("RGB")


def mit_wasserzeichen(bild):
    """Setzt «© Yannic Doutaz» halbtransparent unten rechts ins Bild."""
    ebene = Image.new("RGBA", bild.size, (0, 0, 0, 0))
    zeichnen = ImageDraw.Draw(ebene)
    # Grösse wächst mit dem Bild, damit das Zeichen auf allen Breiten gleich wirkt
    groesse = max(12, round(bild.width * 0.016))
    schrift = ImageFont.truetype(SCHRIFT, groesse, index=0)
    rand = round(groesse * 1.2)
    links, oben, rechts, unten = zeichnen.textbbox((0, 0), WASSERZEICHEN, font=schrift)
    x = bild.width - (rechts - links) - rand
    y = bild.height - (unten - oben) - rand - oben
    # Dunkler Schatten, damit das Zeichen auch auf hellem Himmel lesbar bleibt
    schatten = max(1, groesse // 14)
    zeichnen.text((x + schatten, y + schatten), WASSERZEICHEN, font=schrift, fill=(0, 0, 0, 90))
    zeichnen.text((x, y), WASSERZEICHEN, font=schrift, fill=(255, 255, 255, 150))
    return Image.alpha_composite(bild.convert("RGBA"), ebene).convert("RGB")


def mittlere_farbe(bild):
    """Durchschnittsfarbe als Platzhalter, bis das Foto geladen ist."""
    r, g, b = bild.resize((1, 1), Image.Resampling.BOX).getpixel((0, 0))
    return f"#{r:02x}{g:02x}{b:02x}"


def kurzname(pfad):
    """«Jäger im Nebel.jpg» -> «jaeger-im-nebel»: sicher für URLs."""
    name = pfad.stem.lower()
    for umlaut, ersatz in (("ä", "ae"), ("ö", "oe"), ("ü", "ue"), ("ß", "ss")):
        name = name.replace(umlaut, ersatz)
    name = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", name).strip("-")


def verarbeite(quelle, meta, kategorie):
    """Rechnet ein Foto in alle Breiten und gibt den Manifest-Eintrag zurück."""
    with Image.open(quelle) as original:
        bild = nach_srgb(ImageOps.exif_transpose(original))

    name = kurzname(quelle)
    # Nie hochrechnen: Ist das Original schmaler, ist es selbst die grösste Stufe
    breiten = [b for b in BREITEN if b < bild.width] + [min(bild.width, BREITEN[-1])]
    breiten = sorted(set(breiten))

    ziele = []
    for breite in breiten:
        hoehe = round(bild.height * breite / bild.width)
        stufe = bild.resize((breite, hoehe), Image.Resampling.LANCZOS)
        ziel = AUSGANG / f"{name}-{breite}.webp"
        mit_wasserzeichen(stufe).save(ziel, "WEBP", quality=QUALITAET, method=6)
        ziele.append(ziel)
    schreibe_rechte(quelle, ziele)

    return {
        "datei": name,
        "kategorie": kategorie,
        "breiten": breiten,
        "breite": bild.width,
        "hoehe": bild.height,
        "alt": als_text(meta.get("Description") or meta.get("Caption-Abstract")),
        "titel": als_text(meta.get("Title")),
        "farbe": mittlere_farbe(bild),
    }


# ---------- Ablauf ----------

def lade_manifest():
    if MANIFEST.exists():
        return {f["datei"]: f for f in json.loads(MANIFEST.read_text(encoding="utf-8"))["fotos"]}
    return {}


def speichere_manifest(fotos):
    daten = {"fotos": sorted(fotos.values(), key=lambda f: (f["kategorie"], f["datei"]))}
    MANIFEST.write_text(json.dumps(daten, ensure_ascii=False, indent=4) + "\n", encoding="utf-8")


def aktuell(quelle, eintrag):
    """True, wenn alle Web-Dateien existieren und neuer sind als der Export."""
    if not eintrag:
        return False
    for breite in eintrag["breiten"]:
        ziel = AUSGANG / f"{eintrag['datei']}-{breite}.webp"
        if not ziel.exists() or ziel.stat().st_mtime < quelle.stat().st_mtime:
            return False
    return True


def aufbereiten(alle):
    if not EINGANG.exists():
        sys.exit(f"Ordner fehlt: {EINGANG}\nLege die Lightroom-Exporte dort in Unterordnern pro Kategorie ab.")
    AUSGANG.mkdir(parents=True, exist_ok=True)

    quellen = sorted(p for p in EINGANG.rglob("*") if p.suffix.lower() in ENDUNGEN)
    metadaten = lies_metadaten(quellen)
    fotos = lade_manifest()
    abgelehnt, neu = [], 0

    for quelle in quellen:
        meta = metadaten.get(quelle.resolve(), {})
        fehlt = fehlende_rechte(meta)
        if fehlt:
            abgelehnt.append(f"{quelle.relative_to(EINGANG)}: {' und '.join(fehlt)} fehlt")
            continue
        name = kurzname(quelle)
        if not alle and aktuell(quelle, fotos.get(name)):
            continue
        # Unterordner = Kategorie, Fotos direkt im Eingang landen unter «allgemein»
        kategorie = quelle.parent.name if quelle.parent != EINGANG else "allgemein"
        eintrag = verarbeite(quelle, meta, kategorie)
        if not eintrag["alt"]:
            print(f"Hinweis: {name} hat keine Bildbeschreibung (Lightroom: Bildunterschrift), Alt-Text fehlt.")
        fotos[name] = eintrag
        neu += 1
        print(f"ok  {name}  {eintrag['breiten']}")

    speichere_manifest(fotos)
    print(f"\n{neu} Foto(s) verarbeitet, {len(fotos)} im Manifest.")
    if abgelehnt:
        print("\nNicht verarbeitet, Urheber-Metadaten fehlen (Lightroom-Exportvorgabe prüfen):")
        print("\n".join(f"  - {zeile}" for zeile in abgelehnt))
        sys.exit(1)


def pruefen():
    """Prüft alle Web-Fotos. Exit-Code 1, wenn eines die Urheber-Metadaten nicht trägt."""
    dateien = sorted(AUSGANG.glob("*.webp"))
    metadaten = lies_metadaten(dateien)
    fehler = []
    for datei in dateien:
        fehlt = fehlende_rechte(metadaten.get(datei.resolve(), {}))
        if fehlt:
            fehler.append(f"{datei.relative_to(PROJEKT)}: {' und '.join(fehlt)} fehlt")
    if fehler:
        print("Fotos ohne Urheber-Metadaten:")
        print("\n".join(f"  - {zeile}" for zeile in fehler))
        sys.exit(1)
    print(f"Alle {len(dateien)} Web-Fotos tragen Urheber und Copyright von {URHEBER}.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--alle", action="store_true", help="alle Fotos neu rechnen")
    parser.add_argument("--pruefen", action="store_true", help="nur die Web-Fotos prüfen")
    argumente = parser.parse_args()
    pruefen() if argumente.pruefen else aufbereiten(argumente.alle)
