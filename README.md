# portfolio-page

Portfolioseite von Yannic Doutaz, Einzelarbeit im Modul EWEB Web Engineering (BFH, HS26).

- Live: https://yannicdoutaz.github.io/portfolio-page/
- Stack: reines HTML, CSS, JavaScript (keine Frameworks), gehostet auf GitHub Pages

## Struktur

```
index.html                 Startseite: Hero, Über mich, Skills, Projekte, Kontakt
hauptner-coverfoto.html    Projekt: Coverfoto Herbstkatalog, Hauptner Jagd
reka-abschiedsfilm.html    Projekt: Abschiedsfilm, Reka
galerie.html               Fotogalerie
css/style.css              Design-Tokens, Layout
js/main.js                 Projektkarten und Filter aus data/projekte.json
data/projekte.json         Projektdaten (Titel, Kategorie, Text, Tags, Link)
assets/img/                web-optimierte Bilder
```

Die Bild-Originale liegen in `Webseite - Bilder/` und sind per `.gitignore` von der
Versionierung ausgeschlossen. Ins Repo kommen nur Exporte für das Web.

## Lokal starten

In VS Code mit «Live Server» oder im Projektordner `python3 -m http.server 8080`
und dann `http://localhost:8080` öffnen. Per Doppelklick (`file://`) blockiert der
Browser das Laden von `data/projekte.json`, dann erscheinen nur die zwei statischen
Projektkarten.

## Stand

Inhalte und Struktur stehen. Offen sind Responsivität (Media Queries), JavaScript
(Navigation, Galerie, Formularvalidierung) und die Bilder. Siehe die
[Issues](https://github.com/yannicdoutaz/portfolio-page/issues).

## KI-Nutzung

Im Modul EWEB ist der Einsatz von KI vorgesehen, er muss aber offengelegt werden.
Ab November 2026 arbeite ich an dieser Seite mit Claude (Anthropic, Claude Code).
Claude hilft beim Entwerfen und Prüfen von HTML, CSS und JavaScript, erklärt Code
und recherchiert Bibliotheken und APIs. Ich prüfe jeden Vorschlag, bevor er ins
Repo kommt.

Commits, an denen Claude mitgeschrieben hat, tragen in der Nachricht eine Zeile
`KI: …` mit Angabe, wofür KI eingesetzt wurde.

## Repository-Historie
Ursprünglich auf dem privaten Account angelegt, für das Modul EWEB (BFH) auf den Studienaccount verschoben und im November 2026 zurück auf den privaten Account transferiert, damit das Projekt über das Studium hinaus weitergeführt wird. Der Commit-Verlauf ist vollständig erhalten.
