# Bilder und Dateien auf die Seite bringen

Wie Fotos, fremde Bilder und PDF-Dateien von der Ablage auf die Seite kommen. Ziel: scharfe
Bilder, kurze Ladezeit, klare Urheberschaft. Wer welches Bild gemacht hat und was davon noch
offen ist, steht in [bildrechte.md](../bildrechte.md).

## 1. Welcher Weg für welche Datei?

```mermaid
flowchart TD
    start(["Neue Datei für die Seite"]) --> art{"Was ist es?"}

    art -->|"Eigenes Foto"| eigen["Weg A: Bild-Skript<br/>Wasserzeichen und Urheber-Metadaten"]
    art -->|"Bild von jemand anderem<br/>(Porträt, Screenshot Kunde)"| fremd{"Schriftliche Freigabe<br/>vorhanden?"}
    art -->|"PDF"| pdf{"Öffentlich schon<br/>online verfügbar?"}

    fremd -->|"Nein"| warten["Freigabe einholen,<br/>in bildrechte.md als offen führen"]
    fremd -->|"Ja"| fremdweg["Weg B: von Hand als WebP<br/>ohne Wasserzeichen, mit Nennung"]
    warten -.->|"Freigabe da"| fremdweg

    pdf -->|"Ja, z. B. E-Paper"| link["Weg C1: Vorschaubild<br/>und Link auf die Quelle"]
    pdf -->|"Nein"| pdfweg["Weg C2: verkleinern<br/>und mit PDF.js anzeigen"]
```

## 2. Weg A: eigene Fotos

```mermaid
flowchart LR
    lr["Lightroom<br/>Auswahl und Bearbeitung"] --> export["Export als JPEG<br/>sRGB, 3000 px, Qualität 90+<br/>mit Copyright-Vorgabe"]
    export --> ordner[("Webseite - Bilder/kategorie/<br/>nicht im Repo")]
    ordner --> skript["python3 tools/bilder.py"]
    skript --> pruef{"Urheber und<br/>Copyright drin?"}
    pruef -->|"Nein"| ab["Abgelehnt<br/>Exportvorgabe prüfen"]
    ab -.-> export
    pruef -->|"Ja"| web["4 Breiten als WebP<br/>640, 1280, 1920, 2560 px<br/>Wasserzeichen, ohne GPS"]
    web --> ziel[("assets/img/fotos/<br/>data/fotos.json")]
    ziel --> kontrolle["python3 tools/bilder.py --pruefen"]
    kontrolle --> commit["Commit und Push"]
```

### Export aus Lightroom

| Einstellung | Wert | Grund |
| --- | --- | --- |
| Format | JPEG, Qualität 90 oder höher | Ausgangsmaterial für das Skript, es verkleinert selbst |
| Farbraum | sRGB | Browser zeigen sRGB, andere Profile wirken flau |
| Grösse | lange Kante 3000 px | reicht für die grösste Stufe (2560 px) |
| Schärfen | Bildschirm, Standard | Schärfe nach dem Verkleinern |
| Metadaten | «Alle ausser Kamera- und Camera-Raw-Infos», Standortinfo entfernen | Urheber und Beschreibung bleiben, GPS fällt weg |
| Copyright-Vorgabe | Urheber «Yannic Doutaz», Copyright «© Jahr Yannic Doutaz», Status «urheberrechtlich geschützt» | das Skript lehnt Exporte ohne diese Angaben ab |
| Bildunterschrift | kurze Beschreibung des Bildinhalts | wird zum Alt-Text auf der Seite |
| Wasserzeichen | keines | setzt das Skript, so bleiben die Originale sauber |
| Dateiname | sprechend, z. B. `haslimoos-jaeger-nebel.jpg` | wird zum Namen der Web-Datei |

Der Unterordner bestimmt die Kategorie in der Galerie: `natur`, `auftraege`, `making-of`.

### Warum Wasserzeichen und Metadaten im Bild und nicht auf der Webseite

Ein Wasserzeichen aus CSS liegt nur über dem Bild. Wer das Bild speichert, bekommt es ohne.
Darum setzt das Skript das Zeichen fest in die Pixel. Die Metadaten entstehen beim Export, das
Skript prüft sie zweimal: beim Einlesen (Export ohne Angaben wird abgelehnt) und mit
`--pruefen` über alle Dateien in `assets/img/fotos/`, auch über solche, die jemand von Hand
dorthin kopiert hat.

## 3. Wie der Browser die Fotos lädt

```mermaid
sequenceDiagram
    participant B as Browser
    participant S as GitHub Pages

    B->>S: Seite und data/fotos.json
    Note over B: Platzhalter in der Durchschnittsfarbe,<br/>Höhe steht fest, nichts springt
    B->>S: Vorschau in passender Breite<br/>(srcset: Handy 640 px, Laptop 1280 px)
    Note over B: Bilder unterhalb des Fensters<br/>erst beim Scrollen (loading="lazy")
    B->>S: Klick auf ein Bild: Grossansicht<br/>1920 oder 2560 px je nach Bildschirm
```

Mit `srcset` und `sizes` wählt der Browser selbst die kleinste Datei, die auf seinem
Bildschirm noch scharf ist, auch auf Retina-Bildschirmen. Die grossen Stufen lädt nur, wer
ein Bild öffnet.

## 4. Weg B: Bilder von anderen

Gilt für das Porträt (Stefan Wermuth) und für Screenshots aus dem Katalog von Hauptner Jagd.

- Erst verwenden, wenn die Freigabe schriftlich vorliegt (Stand in [bildrechte.md](../bildrechte.md)).
- Kein Wasserzeichen mit meinem Namen und nicht in `assets/img/fotos/`, das Skript würde sie zu Recht ablehnen.
- Ablage in `assets/img/fremd/`, als WebP verkleinert, z. B. `cwebp -q 80 -resize 1600 0 eingang.png -o assets/img/fremd/name.webp`.
- Nennung direkt beim Bild (`<figcaption>`), mit Link, wenn die Person es wünscht.

## 5. Weg C: PDF-Dateien

```mermaid
flowchart LR
    q{"Gibt es eine<br/>öffentliche Fassung?"} -->|"Ja"| c1["C1: Vorschaubild der Titelseite<br/>und Link «Katalog ansehen»"]
    q -->|"Nein"| gs["Ghostscript verkleinern<br/>Bilder auf 150 dpi, Fast Web View"]
    gs --> ablage[("assets/pdf/")]
    ablage --> vorschau["Seite zeigt zuerst nur<br/>ein Vorschaubild"]
    vorschau -->|"Klick"| pdfjs["PDF.js lädt nach<br/>und zeigt Seite für Seite"]
```

- **C1, Hauptner-Katalog:** Der Katalog ist als E-Paper öffentlich
  ([yumpu.com](https://www.yumpu.com/de/document/read/67102472/j1-jagd-katalog)). Die Seite
  zeigt einen Screenshot der Titelseite (Weg B) und verlinkt das E-Paper. Kein eigener
  Upload, keine Einbettung: Die Einbettung von Yumpu bringt Werbung und Tracker mit.
- **C2, eigene PDFs:** verkleinern mit
  `gs -sDEVICE=pdfwrite -dPDFSETTINGS=/ebook -dFastWebView=true -o assets/pdf/name.pdf eingang.pdf`.
  «Fast Web View» ordnet die Datei so, dass PDF.js die erste Seite zeigen kann, bevor der
  Rest geladen ist. PDF.js wird erst beim Klick geladen, die Seite bleibt bis dahin leicht.
  Status: zurzeit nicht nötig, der einzige Katalog läuft über C1.
