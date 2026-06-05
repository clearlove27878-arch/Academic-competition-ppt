# Visual Long Deck QA

Use this after rendering previews/contact sheet for any long-form paper deck.

## Pagination QA

- Total page count in page markers is correct.
- No `current/old_total` errors after adding or removing pages.
- Section navigation and page numbers agree with the slide inventory.

## Title QA

- Main titles are usually 6-14 Chinese characters.
- Titles over 18 Chinese characters are split into title + subtitle.
- Card titles are 2-8 Chinese characters and parallel where possible.

## Readability QA

- Main title: 30-40 pt.
- Chapter title: 36-48 pt.
- Subtitle/guide sentence: 18-24 pt.
- Body paragraphs: 16-20 pt.
- Card body: 14-17 pt.
- Table body: 11-14 pt.
- Left short nav title: about 16-20 pt when space allows.
- Active chapter nav chip: about 12-16 pt when space allows.
- Inactive chapter nav chip: about 10-14 pt, usually 2 pt smaller than active, when space allows.
- Footnote/source: 8-10 pt.
- Content below 10 pt is not core information.

## Navigation QA

- Top navigation is present on ordinary content pages.
- Navigation occupies about 6%-9% of slide height.
- All navigation labels use `思源宋体 CN Heavy` or the same Source Han Serif family; do not mix sans, serif, and decorative fonts in one navigation row.
- Active section is deep teal/yellow, bold, clear, and about 12-16 pt when space allows.
- Inactive labels/chips are deep gray/deep teal, readable, visually lighter, and about 10-14 pt when space allows.
- Active underlines, color blocks, chips, or soft highlights may use restrained gradients, light shadows, translucent overlays, or soft strokes for polish.
- Navigation highlights must not press into the title/body area or reduce reading contrast.
- Repeated double-triangle or arrow markers are acceptable only when integrated into a designed header system.

## Bottom Bar And Background QA

- Ordinary content pages have a bottom takeaway bar unless there is a documented special layout.
- Bottom bar height is about 4%-7%.
- Bottom-bar decoration may include arcs, leaves, arrows, geometric blocks, corner motifs, or repeated motifs when they are low-opacity, low-area, and secondary to the takeaway.
- Bottom-bar text remains the visual priority; decoration must not crowd, cover, or compete with it.
- Bottom-bar blocks, pale bands, corner fills, and deep-teal title bars may use soft gradients, translucent overlays, light shadows, and soft strokes to avoid flat coarse color blocks.
- Background decoration is visible but subtle; ordinary pages are not pure white empty canvases.
- Decoration does not interfere with text, evidence, or tables.
- Transparent rounded content containers may use low-contrast gradient fills, gradient-like edge layers, translucent strokes, or light shadows.
- Gradients and shadows do not reduce body text, table, or formula readability.

## Density And Rhythm QA

- Ordinary content pages reach about 65%-85% visual fill.
- Pages below 60% are fixed with source paragraphs, paper objects, explanation panels, bottom takeaway, or decoration.
- Adjacent 5 pages are not fully isomorphic.
- Every 6-8 pages includes a rhythm change.

## Evidence QA

- Tables are readable and not shrunk into decoration.
- Formula panels are large, with symbol/meaning and boundary explanations.
- Research-plan result pages preserve cautious wording such as `拟检验`, `待估计`, and `若结果显示`.
- Contact sheet is checked for blankness, font size, navigation, page count, decoration, repeated layout, and title length.
