# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Primär: künftige Arbeitgeberinnen, Arbeitgeber und Recruiter aus Tech, technischem Support und Digital Business. Sie prüfen in kurzer Zeit, ob Yannic Doutaz technisch und gestalterisch zu einer Stelle passt, und wollen dafür echte Projekte sehen statt Behauptungen.

Erster Prüfstein ist die Bewertung im Modul EWEB (BFH, HS26). Die Seite wird über das Studium hinaus weitergeführt.

Daneben: Firmen und Private, die einen Foto- oder Videoauftrag vergeben möchten.

## Product Purpose

Persönliche Portfolioseite von Yannic Doutaz. Sie zeigt ausgewählte Projekte aus Fotografie und Video, Automatisierung und KI sowie dem Studium.

Erfolg heisst: Besuchende
- vertiefen sich in die Projekte und verstehen, wie Yannic arbeitet,
- sehen sich die Fotos an,
- fragen einen Auftrag an.

## Positioning

Technik und Gestaltung verbinden: im Beruf mit Support-Prozessen, Automatisierung und Web, in der Freizeit mit Kamera und Schnitt. Die Seite belegt beide Seiten mit eigenen, real umgesetzten Projekten.

## Operating Context

- Erreichbar über GitHub Pages: https://yannicdoutaz.github.io/portfolio-page/
- Besuchende kommen auf Desktop, Tablet und Mobile.
- Sprache der Seite: Deutsch (Schweizer Rechtschreibung, «ss» statt «ß»), Ansprache per Du.

## Capabilities and Constraints

- Seiten: Startseite (Hero, Über mich, Skills, Projekte, Kontakt), Fallstudien-Unterseiten pro Projekt, Galerie.
- Projektdaten liegen in `data/projekte.json`; Karten und Kategorie-Filter entstehen per JavaScript. Scheitert das Laden, bleiben statische Karten im HTML stehen.
- Kontaktformular mit Versand über Formspree (Endpoint noch nicht eingerichtet).
- Stack: reines HTML, CSS und JavaScript ohne Framework, statisch gehostet. Kein eigener Server.
- Muss auf allen Bildschirmgrössen ohne abgeschnittene Inhalte und ohne horizontale Scrollleiste funktionieren.
- Abgabe am 18.12.2026; danach keine Commits mehr im Repository.
- Arbeitsprojekte dürfen nur anonymisiert erscheinen: keine Kunden-, Ticket- oder Personendaten, keine Server-URLs oder IDs, kein Firmenname in der Meta-Zeile.
- KI-Einsatz wird offengelegt (README, Commit-Nachrichten). Übernommene oder angelehnte Quellen werden auf der Seite genannt. Das ist eine Projektregel, kein Verkaufsargument der Seite.
- Offen: ob eine Projektvorlage `projekt.html?id=…` die einzelnen Unterseiten ablöst.

## Brand Commitments

- Name: Yannic Doutaz. Seitentitel «Technik und Gestaltung».
- Fotos und Videos stammen von Yannic Doutaz selbst.

## Evidence on Hand

- Acht reale Projekte in `data/projekte.json`, davon zwei Kundenaufträge mit eigener Unterseite (`hauptner-coverfoto.html`, `reka-abschiedsfilm.html`).
- Eigene Fotos und Videostills; die Originale liegen lokal und sind nicht versioniert, Web-Exporte folgen in `assets/img/`.
- Noch nicht vorhanden: Porträtfoto, Bilder auf der Seite, Fallstudien für die Projekte aus Automatisierung, KI und Studium.
- Keine Testimonials, Kundenstimmen, Kennzahlen oder Auszeichnungen vorhanden. Nichts davon erfinden.

## Product Principles

1. Belegen statt behaupten: Jede Fähigkeit hängt an einem echten Projekt.
2. Beide Seiten gleich ernst nehmen: Technik und Gestaltung stehen nebeneinander, keine ist nur Beigabe.
3. Ehrlich über den eigenen Anteil: Bei Gruppen- und Arbeitsprojekten steht klar, was Yannic selbst gemacht hat.
4. Funktioniert überall: Inhalte bleiben auf jedem Gerät vollständig und lesbar, auch wenn JavaScript oder das Laden der Daten scheitert.
