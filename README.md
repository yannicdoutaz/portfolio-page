# portfolio-page

Portfolioseite von Yannic Doutaz, Einzelarbeit im Modul EWEB Web Engineering (BFH, HS26).

- Live: https://yannicdoutaz.github.io/portfolio-page/
- Stack: reines HTML, CSS, JavaScript (keine Frameworks), gehostet auf GitHub Pages

## Struktur

```
index.html                 Startseite: Hero mit Bildmosaik, Über mich, Bereiche, Projekte, Kontakt
hauptner-coverfoto.html    Projekt: Coverfoto Herbstkatalog, Hauptner Jagd
reka-abschiedsfilm.html    Projekt: Abschiedsfilm, Reka
galerie.html               Fotogalerie
css/style.css              Design-Tokens, Layout
js/main.js                 Projektkarten und Filter aus data/projekte.json
data/projekte.json         Projektdaten (Titel, Kategorie, Text, Tags, Link)
assets/img/                web-optimierte Bilder: Porträt und Logo von Yannic Doutaz
docs/design/               Design-Prozess in Figma und Design-Entscheide
```

Die Bild-Originale liegen in `Webseite - Bilder/` und sind per `.gitignore` von der
Versionierung ausgeschlossen. Ins Repo kommen nur Exporte für das Web.

## Fotos aufbereiten

`tools/bilder.py` macht aus den Lightroom-Exporten in `Webseite - Bilder/<kategorie>/`
Web-Fotos in `assets/img/fotos/`: vier Breiten (640 bis 2560 px) als WebP für `srcset`,
Wasserzeichen unten rechts, Urheber und Copyright in den Metadaten, ohne GPS-Daten.
Die Liste für die Galerie steht danach in `data/fotos.json`.

```
python3 tools/bilder.py            neue und geänderte Fotos verarbeiten
python3 tools/bilder.py --pruefen  prüfen, ob alle Web-Fotos die Urheber-Metadaten tragen
```

Ein Export ohne Urheber und Copyright in den Metadaten wird abgelehnt. Braucht Pillow
und exiftool. Den ganzen Ablauf für Fotos, fremde Bilder und PDFs als Diagramm zeigt
[docs/prozess/bilder-und-dateien.md](docs/prozess/bilder-und-dateien.md), Urheber und
offene Freigaben stehen in [docs/bildrechte.md](docs/bildrechte.md).

## Lokal starten

In VS Code mit «Live Server» oder im Projektordner `python3 -m http.server 8080`
und dann `http://localhost:8080` öffnen. Per Doppelklick (`file://`) blockiert der
Browser das Laden von `data/projekte.json`, dann erscheinen nur die zwei statischen
Projektkarten.

## Stand

Die Startseite ist im Stil «Moos bei Nacht» gestaltet
([Design-Entscheid 003](docs/design/entscheide/003-visuelle-welt-moos-bei-nacht.md)),
responsiv und mit Menü für das Handy. Offen sind echte Projektbilder, die Unterseiten im
neuen Stil, die Galerie sowie Versand und Validierung des Formulars. Siehe die
[Issues](https://github.com/yannicdoutaz/portfolio-page/issues).

Schriften: Anton und Familjen Grotesk (SIL Open Font License), derzeit über Google Fonts
eingebunden.

## KI-Nutzung

Im Modul EWEB ist der Einsatz von KI vorgesehen, er muss aber offengelegt werden.
Ab November 2026 arbeite ich an dieser Seite mit Claude (Anthropic, Claude Code).
Claude hilft beim Entwerfen und Prüfen von HTML, CSS und JavaScript, erklärt Code
und recherchiert Bibliotheken und APIs. Für das Redesign hat Claude Gestaltungsvarianten
in Figma entworfen und die gewählte Variante in HTML, CSS und JavaScript umgesetzt. Ich
prüfe jeden Vorschlag, bevor er ins Repo kommt.

Commits, an denen Claude mitgeschrieben hat, tragen in der Nachricht eine Zeile
`KI: …` mit Angabe, wofür KI eingesetzt wurde.

## Repository-Historie
Ursprünglich auf dem privaten Account angelegt, für das Modul EWEB (BFH) auf den Studienaccount verschoben und im November 2026 zurück auf den privaten Account transferiert, damit das Projekt über das Studium hinaus weitergeführt wird. Der Commit-Verlauf ist vollständig erhalten.
