# Long Paper Deck QA

Use this before delivering a default long-form paper presentation.

## Chain Coverage

- Problem chain is visible: puzzle, contradiction, research question, why it matters.
- Concept chain is visible: definitions, measurement, model role, common confusion.
- Identification chain is visible: naive method, bias/threat, chosen method, assumption, boundary.
- Result chain is visible: baseline/expected test, mechanism, heterogeneity, robustness/endogeneity, contribution.

## Source Fidelity

- Core pages contain source anchors or faithful paraphrases.
- Technical pages preserve original model meaning.
- Background pages do not overstate facts.
- Low-value literature or boilerplate did not crowd out core logic.
- Each major chapter derives about 40%-60% of body content from original anchors, original viewpoints, or faithful paraphrases.
- Each ordinary page has at least one original thought object, not just framework labels.

## Formula And Model QA

- Each formula answers a clear question.
- Variables and key coefficients are explained.
- Fixed effects, controls, instruments, matching, event-time terms, or other design pieces have a plain-language purpose.
- Model boundaries are stated when important.

## Results QA

- Each result page answers a previous question.
- Tables/figures are readable or split/cropped.
- Coefficients, directions, significance, or expected directions are not fabricated.
- Research-plan decks use `拟检验`, `预期方向`, `待估计`, or `若结果显示`.

## Long-Deck Rhythm

- No long run of identical card grids.
- Every 6-8 pages has a rhythm change, recap, transition, close-up, or synthesis.
- Navigation and breadcrumbs help the audience know where they are.
- Dense text exists only when it carries explanation and remains readable.
- Adjacent 5 pages do not use the exact same layout.

## Technical QA

- Chinese visible text has no `????`, mojibake, or replacement characters.
- Formula fallback was used when editable math was unstable.
- PPTX key research content is editable where practical.
- Images, tables, screenshots, and charts preserve aspect ratio.
- Contact sheet and individual previews show no overlap, clipping, or unreadable evidence.
- Visual long-deck QA in `qa-visual-long-deck.md` passes: page count, navigation, title length, bottom bar, decoration, fill ratio, and repeated layouts.

## Font QA

- Cover, chapter, page title, and navigation fonts follow the font role system.
- Body paragraphs do not use decorative fonts or Heavy title fonts.
- Tables, labels, page numbers, footnotes, and captions use readable sans fonts.
- English paper information, references, and English quotes use Times New Roman or fallback.
- Decorative fonts are local accents only and stay within the allowed page/style limits.
- Missing fonts fall back without Chinese glyph loss, text overflow, formula errors, or export damage.
