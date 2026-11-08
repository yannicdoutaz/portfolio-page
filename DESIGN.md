---
name: Yannic Doutaz · Technik und Gestaltung
description: Persönliche Portfolioseite, heller und neutraler Rahmen, in dem Fotos und Projekte die Farbe tragen.
colors:
  bg: "#ffffff"
  bg-alt: "#f4f4f2"
  text: "#1b1b1a"
  text-leise: "#6b6b66"
  linie: "#dcdcd6"
  akzent: "#3f6b4f"
  akzent-kontrast: "#ffffff"
typography:
  display:
    fontFamily: "system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "clamp(1.75rem, 4vw, 2.75rem)"
    fontWeight: 700
    lineHeight: 1.2
  headline:
    fontFamily: "system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "1.5rem"
    fontWeight: 700
    lineHeight: 1.6
  title:
    fontFamily: "system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "1.17rem"
    fontWeight: 700
    lineHeight: 1.6
  body:
    fontFamily: "system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.6
  label:
    fontFamily: "system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "0.875rem"
    fontWeight: 400
    lineHeight: 1.6
rounded:
  sm: "4px"
spacing:
  xs: "0.5rem"
  s: "0.75rem"
  m: "1.25rem"
  l: "2rem"
  xl: "4rem"
components:
  filter-chip:
    backgroundColor: "{colors.bg}"
    textColor: "{colors.text}"
    typography: "{typography.label}"
    rounded: "{rounded.sm}"
    padding: "0.5rem 0.75rem"
  filter-chip-active:
    backgroundColor: "{colors.akzent}"
    textColor: "{colors.akzent-kontrast}"
    typography: "{typography.label}"
    rounded: "{rounded.sm}"
    padding: "0.5rem 0.75rem"
  card:
    backgroundColor: "{colors.bg}"
    textColor: "{colors.text}"
    rounded: "{rounded.sm}"
    padding: "0.5rem 1.25rem"
  tag:
    backgroundColor: "{colors.bg-alt}"
    textColor: "{colors.text}"
    typography: "{typography.label}"
    rounded: "{rounded.sm}"
    padding: "0 0.5rem"
---

<!-- REFERENZ: Bestandsaufnahme des Designs vom 8.11.2026, vor einem geplanten Redesign. Neue Gestaltung entsteht über eine neue visuelle Welt (/impeccable mit new-work) und ersetzt diese Datei dann. Bis dahin beschreibt sie verbindlich, wie die Seite heute aussieht. -->

# Design System: Yannic Doutaz · Technik und Gestaltung

## Overview

**Creative North Star: "Das Passepartout"**

Die Seite ist der weisse Karton um ein gerahmtes Bild. Sie tritt zurück, damit Fotos und Projekte wirken: viel Weissraum, eine einzige ruhige Schrift, feine Linien statt Flächen. Farbe kommt aus den Bildern, nicht aus der Oberfläche.

Die Dichte ist niedrig, alles steht in einer schmalen Lesespalte. Die Haltung ist sachlich und zurückhaltend, eher Werkverzeichnis als Werbeplakat.

Stand heute ist das System ein Gerüst: Farb-, Schrift- und Abstandstokens stehen, Projektkarten und Filter sind gestaltet. Navigation, Textlinks, Hero-Aktionen und das Kontaktformular laufen noch mit Browser-Standard. Bilder fehlen noch ganz.

**Key Characteristics:**
- Hell und neutral, warm getöntes Grau statt reinem Grau.
- Ein einziger Akzent (Waldgrün), sparsam für Zustand und Kategorie.
- Flach: Linien und Tonflächen, keine Schatten.
- Systemschrift, Hierarchie nur über Grösse und Gewicht.
- Kleine, gleichmässige Rundung (4px) an allem, was eine Kante hat.

## Colors

Fast farblos: warmes Papierweiss, Tusche und drei Graustufen, dazu ein gedecktes Grün als einzige Stimme.

### Primary
- **Waldgrün** (#3f6b4f): Zustand und Zuordnung. Aktiver Filterknopf (Fläche), Hover auf Links und Filterknöpfen, Kategoriezeile über dem Kartentitel.

### Neutral
- **Papierweiss** (#ffffff): Seitenhintergrund und Kartenfläche.
- **Passepartout-Grau** (#f4f4f2): leicht warme Tonfläche für Tags.
- **Tusche** (#1b1b1a): Fliesstext und Überschriften.
- **Bleistiftgrau** (#6b6b66): Meta-Zeilen (Auftraggeber, Art, Jahr).
- **Kartonlinie** (#dcdcd6): Kartenrahmen, Filterrahmen, Trennlinie über dem Footer.
- **Akzent-Kontrast** (#ffffff): Text auf Waldgrün.

### Named Rules
**The Bild-zuerst Rule.** Die Oberfläche bleibt neutral, damit die Bilder die einzigen Farbflächen sind. Keine farbigen Hintergründe, Verläufe oder Illustrationsfarben.

**The Eine-Stimme Rule.** Waldgrün ist der einzige Akzent. Es zeigt einen Zustand oder eine Zuordnung, nie Dekoration.

## Typography

**Body Font:** system-ui (mit -apple-system, Segoe UI, sans-serif)

**Character:** Eine Schrift für alles, die Systemschrift des Geräts. Neutral und schnell, sie drängt sich nicht vor die Inhalte.

### Hierarchy
- **Display** (700, clamp(1.75rem, 4vw, 2.75rem), 1.2): nur der Name im Hero und der Titel einer Projekt-Unterseite.
- **Headline** (700, 1.5rem, 1.6): Abschnittstitel wie «Über mich», «Projekte», «Kontakt». Heute Browser-Standard, nicht als Token gesetzt.
- **Title** (700, 1.17rem, 1.6): Kartentitel und Skill-Gruppen. Heute Browser-Standard.
- **Body** (400, 1rem, 1.6): Fliesstext. Die Lesespalte ist auf 70ch begrenzt; Ziel für Textblöcke sind 65–75ch.
- **Label** (400, 0.875rem): Meta-Zeilen, Kategorie, Tags, Filterknöpfe.

### Named Rules
**The Gewicht-statt-Schrift Rule.** Hierarchie entsteht über Grösse und Gewicht derselben Schrift, nicht über eine zweite Familie.

## Layout

Eine zentrierte Spalte (max. 70ch, Innenabstand 1.25rem) trägt alle Inhalte. Abschnitte stehen mit 4rem Abstand untereinander. Header und Footer laufen über die volle Breite.

Das Projektraster ist das einzige Raster: `repeat(auto-fill, minmax(min(100%, 18rem), 1fr))` mit 0.75rem Abstand. Es wechselt ohne Media Query von einer auf zwei Spalten. Die Filterleiste bricht mit Flexbox um.

Abstände folgen einer festen Skala: 0.5rem, 0.75rem, 1.25rem, 2rem, 4rem. Es gibt noch keine Media Queries; die Navigation steht auch mobil als Zeile von Textlinks.

## Elevation & Depth

Das System ist flach. Es gibt keinen einzigen Schatten. Tiefe und Gruppierung entstehen über 1px Kartonlinie und die Tonfläche Passepartout-Grau.

### Named Rules
**The Linie-statt-Schatten Rule.** Flächen trennen sich durch eine feine Linie oder einen Tonwechsel, nie durch Schatten.

## Shapes

Eine Rundung für alles: sanft abgerundete Ecken (4px) an Karten, Filterknöpfen und Tags. Rahmen sind 1px stark. Keine Pillenform, keine Kreise, keine schrägen Kanten.

## Components

### Chips (Filterknöpfe)
- **Style:** Papierweiss mit 1px Kartonlinie, Label-Grösse, Innenabstand 0.5rem × 0.75rem, 4px Rundung.
- **Hover:** Rahmen wechselt auf Waldgrün.
- **Aktiv** (`aria-pressed="true"`): Fläche und Rahmen Waldgrün, Text weiss.

### Cards / Containers (Projektkarten)
- **Corner Style:** 4px.
- **Background:** Papierweiss.
- **Shadow Strategy:** keine, siehe Elevation & Depth.
- **Border:** 1px Kartonlinie.
- **Internal Padding:** 0.5rem oben/unten, 1.25rem seitlich.
- **Aufbau:** Kategorie (Label, Waldgrün), Titel mit Link, Meta-Zeile (Bleistiftgrau), Text, Tags.

### Tags
- **Style:** Passepartout-Grau, kein Rahmen, Label-Grösse, 4px Rundung, seitlich 0.5rem, eng gesetzt (0.25rem Abstand).

### Inputs / Fields
- **Style:** heute Browser-Standard (Arial, graue Rahmen). Breite 100 %, höchstens 400px. Labels stehen als Block über dem Feld.
- **Lücke:** Fokus-, Fehler- und Erfolgszustände sind noch nicht gestaltet.

### Navigation
- **Style:** Zeile aus Textlinks im Header, Abstand 1.25rem. Heute Browser-Blau, Hover Waldgrün. Kein aktiver Zustand, keine mobile Variante.

## Do's and Don'ts

### Do:
- **Do** neue Farben nur aus den Tokens in `css/style.css` nehmen (`--farbe-…`).
- **Do** Abstände nur aus der Skala `--abstand-xs` bis `--abstand-xl` setzen.
- **Do** Waldgrün (#3f6b4f) für Zustand und Zuordnung reservieren.
- **Do** Fliesstext auf 65–75ch begrenzen.

### Don't:
- **Don't** Schatten einsetzen; Trennung läuft über 1px Kartonlinie (#dcdcd6) oder Passepartout-Grau (#f4f4f2).
- **Don't** farbige Flächen oder Verläufe in die Oberfläche bringen, solange dieses System gilt.
- **Don't** eine zweite Schriftfamilie oder eine zweite Rundung einführen.
- **Don't** diese Datei als Ziel eines Redesigns behandeln; sie ist die Referenz, von der ein Redesign sich lösen darf.
