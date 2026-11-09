# Design-Prozess

Das Design der Seite entsteht in Figma. Ins Repo kommt, was sich daraus für den Code
ergibt: die Tokens, die Entscheide und Screenshots der gewählten Varianten.

- **Figma-Datei:** [Portfolio Design](https://www.figma.com/design/2t7VKj9aWQhTEDvceIYfvy)
- **Tokens im Code:** `css/style.css`, Block `:root` (später `css/tokens.css`)
- **Gestaltungsregeln für die Umsetzung:** [`DESIGN.md`](../../DESIGN.md)
- **Produktrahmen (Zielgruppe, Zweck):** [`PRODUCT.md`](../../PRODUCT.md)

## Ablauf

1. **Ausprobieren in Figma.** Varianten stehen nebeneinander auf einer Seite und
   werden dort verglichen, kommentiert und überarbeitet.
2. **Entscheiden.** Ist eine Variante gewählt, bekommt sie in Figma eine benannte
   Version (z. B. «001 Visuelle Welt gewählt») und im Repo eine Entscheid-Notiz in
   [`entscheide/`](entscheide/) mit Screenshot in `bilder/`.
3. **Übertragen.** Farben, Schriften, Abstände und Rundungen sind in Figma als
   Variables angelegt. Sie werden als CSS Custom Properties in den Code übernommen.
   Der Code liest nur diese Tokens, keine fest eingetragenen Werte.
4. **Prüfen.** Die umgesetzte Seite wird im Browser auf Desktop, Tablet und Mobile
   geprüft. Abweichungen gehen zurück nach Figma oder werden als Entscheid notiert.

Jeder Entscheid ist ein eigener Commit.

## Warum die Figma-Datei nicht im Repo liegt

Figma-Dateien liegen in der Cloud und sind als Export binär. Git könnte nur zeigen,
dass sich etwas geändert hat, nicht was. Nachvollziehbar wird der Prozess über die
Entscheid-Notizen, die Screenshots und die Token-Änderungen im CSS.

## Vorlage für Entscheide

Datei `entscheide/NNN-stichwort.md`:

```markdown
# NNN Titel

- Datum: JJJJ-MM-TT
- Status: entschieden | ersetzt durch NNN
- Figma: Link auf Seite oder Frame, Version

## Ausgangslage
Was war zu klären, und warum jetzt?

## Varianten
- A: …
- B: …

## Entscheid
Gewählt ist …, weil …

## Folgen für den Code
Welche Tokens, Komponenten oder Seiten ändern sich?
```
