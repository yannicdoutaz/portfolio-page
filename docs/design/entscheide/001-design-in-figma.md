# 001 Design in Figma erarbeiten

- Datum: 2026-11-09
- Status: entschieden
- Figma: [Portfolio Design](https://www.figma.com/design/2t7VKj9aWQhTEDvceIYfvy)

## Ausgangslage

Die Seite soll neu gestaltet werden. [`DESIGN.md`](../../../DESIGN.md) hält den Stand
vom 8.11.2026 nur als Referenz fest. Gestaltungsideen kommen laufend dazu. Würde jede
Idee direkt im HTML, CSS und JavaScript ausprobiert, müsste der Code immer wieder
umgebaut werden.

## Varianten

- A: Direkt im Code gestalten und im Browser vergleichen.
- B: In Figma gestalten, Varianten nebeneinander vergleichen und erst die gewählte
  Lösung in den Code übertragen.

## Entscheid

Gewählt ist B. In Figma lassen sich Farben, Schriften, Bausteine und Abläufe schnell
ausprobieren, nebeneinander vergleichen, kommentieren und versionieren. Die Figma-
Variables bilden danach die Grundlage für die Tokens im Code.

Die Figma-Datei selbst kommt nicht ins Repo. Dokumentiert wird über Entscheid-Notizen,
Screenshots und die Token-Änderungen im CSS, siehe [Design-Prozess](../README.md).

## Folgen für den Code

- Gestaltungsänderungen am Code erst, wenn der Entscheid in Figma gefallen ist.
- Funktionen, die nicht vom Aussehen abhängen (mobile Navigation, Formularvalidierung),
  laufen parallel weiter.
- Nach dem ersten Gestaltungsentscheid wird `DESIGN.md` aus den Figma-Variables neu
  geschrieben.
