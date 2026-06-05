# Quality Checklist

Use this before delivering a deck.

## Story

- Every slide has a claim, proof object, and takeaway.
- Every slide has an audience cognition task and a logical position in the paper explanation.
- The deck answers: what is the puzzle, why does it matter, how is it identified, what is found, why does it happen, where does it vary, and what should be done.
- The problem chain, concept chain, identification chain, and result chain are all visible.
- Core pages include source anchors or faithful paraphrases of the paper's original ideas.
- Each major chapter derives about 40%-60% of body copy from source anchors, original viewpoints, or faithful paraphrases.
- Each ordinary page includes at least one original thought object.
- The page count is earned. No two adjacent pages should feel like the same layout with changed text.
- In long-form 50-70 slide decks, each micro-slide explains one distinct paper detail: one formula step, variable group, test, figure, table, doubt, or interpretation.
- Long-form decks include section recaps, transition questions, or logic-chain returns every 6-8 slides so the audience does not lose the thread.

## Style Fidelity

- The deck follows the active style contract: default academic style when no style is specified, or the selected `references/style_*.md` card when Style Extension Mode is active.
- Default decks use the refined deep-teal academic palette with clear navigation, readable evidence containers, yellow active-section accents, and controlled decoration.
- Content pages have a clear top section navigation unless the page is a special cover/closing.
- Top navigation is visually designed as a chapter positioning system, occupies about 7%-10% of slide height when needed, and is not tiny page-header text.
- Active navigation matches the current section and is anchored by a yellow chip, deep-teal treatment, underline, or short color block.
- Navigation labels use one Source Han Serif family, preferably `思源宋体 CN Heavy`; the left short title is about 16-20 pt, active chapter chips are about 12-16 pt, and inactive chips are about 10-14 pt when space allows.
- Inactive chips are normally about 2 pt smaller than active chips and visibly lighter without disappearing.
- Ordinary content pages have a bottom takeaway bar, gradient footer, or equivalent corner chrome.
- Background decoration is subtle but visible; ordinary content pages are not large pure-white empty canvases.
- Bottom-bar, corner chrome, title bars, and navigation highlights may use restrained gradients, light shadows, translucent overlays, and soft strokes for polish.
- Decorative arcs, leaves, arrows, geometric pieces, or corner motifs are acceptable when low-opacity, low-area, and secondary to takeaway/body text.
- If a catalog style is active, verify its color system, navigation rule, density rule, and prohibitions in the selected style card.
- Titles use a clear academic hierarchy; body uses readable Chinese serif/sans fonts as appropriate.
- The visual system feels like polished Chinese academic competition work, not a business template.
- In long-form decks, the competition frame remains visible: navigation bar, background/chrome, current module label, page marker, and logic-chain cues.
- Ordinary courseware mode is used only if the user explicitly requested it.
- If a new template/reference style is active, the deck follows the Template Style Brief rather than the default teal/gold system.
- If a new template conflicts with research readability, deviations are documented as intentional adjustments.

## Readability

- Main title readable at thumbnail size.
- Main title is usually 6-14 Chinese characters; titles over 18 characters are split into title + subtitle.
- Body text mostly 16 pt or larger; 14-15 pt is reserved for secondary notes, captions, and side callouts.
- Core information never uses text below 10 pt.
- Body paragraphs use readable sans fonts; Heavy title fonts and decorative fonts are not used for long text.
- Navigation uses one formal Source Han Serif title/nav font family, never decorative fonts.
- Regression tables remain readable; if not, crop, simplify, or split.
- Equations are large enough to read and paired with interpretation.
- No dense paragraph walls.
- In long-form mode, do not shrink content to avoid adding pages. Add another micro-slide instead.
- Top navigation labels are readable and visually fill their tabs; current section highlight is obvious.
- Source figures, tables, screenshots, and PDF crops preserve their original aspect ratio.
- Text-bearing images are not stretched, squashed, or cropped through captions, axes, notes, or table significance markers.
- Paper evidence images are large enough to function as the main proof object, not small thumbnails.
- Safe white margins, PDF page furniture, and irrelevant blank areas around original figures/tables have been cropped when doing so improves readability.
- If a table/figure is still too small after safe cropping and scaling, it is split into full-context and focused close-up slides.
- Title, accent bar, kicker badge, content cards, and body text do not overlap.
- Kicker badges sit in their own safe zone above or beside the card, never on top of the card border or body text.
- Ordinary content pages visually fill about 65%-85% of the canvas; pages below 60% are revised.

## Empirical Integrity

- No invented coefficients, sample sizes, or significance levels.
- Research plans do not turn expected tests into completed empirical findings.
- Missing data is marked as a placeholder.
- Regression interpretation matches sign and significance.
- Robustness, mechanism, and heterogeneity pages state what each test proves.

## PPTX Editability

- Key text is editable.
- Simple tables are native tables where possible.
- Mechanism diagrams use editable shapes/connectors.
- Decorative backgrounds may be rasterized, but research content should not be flattened into screenshots.

## Template Transfer

- A Template Style Brief exists when the user provided a new template, PPT, screenshot, or "follow this style" request.
- Reference files were inspected without being modified.
- The output matches the active reference in cover logic, page chrome, title hierarchy, color system, and body-page rhythm.
- Small screenshot references are treated as partial style input; the deck does not invent unseen page types.
- Original paper figures/tables remain primary evidence even when framed in the active template style.

## Final QA

- Render PNG previews/contact sheet.
- Run `references/qa-long-paper-deck.md` as the default long-form paper audit.
- Run `references/qa-visual-long-deck.md` as the default visual/pagination audit.
- Run the font role QA in `references/font_usage_rules.md`.
- Compare cover, content page, empirical page, conclusion page, and thanks page against the style rules.
- If a new template/reference style is active, compare cover-to-cover, chapter-to-chapter, body-to-body, table/figure-to-table/figure, and closing-to-closing.
- For 50-70 slide decks, inspect at least one contact sheet per 24 slides and check chapter pacing, not just individual slides.
- For long-form competition-frame decks, verify at least one chapter divider, recap, transition question, or logic-chain return every 6-8 slides.
- Verify adjacent 5 pages do not use a fully identical layout.
- Verify page markers use the correct total page count after every page-count change.
- Verify bottom takeaway bars are present on ordinary content pages.
- Verify background decoration and footer/header chrome have not disappeared.
- Verify bottom-bar decoration does not occupy too much area or distract from the takeaway.
- Verify gradient/shadow effects in navigation, bottom bars, and rounded content containers do not reduce readability.
- Verify dense technical pages still show their place in the argument through a breadcrumb, nav highlight, or stage label.
- Verify full logic-chain diagrams appear only on roadmap, transition, recap, synthesis, or conclusion pages.
- Verify white/no-fill cards have light shadows, and cards/navigation/figure containers use restrained rounded corners rather than sharp default rectangles.
- Verify the full logic-chain diagram appears on exactly one dedicated page unless the user requested repeated recaps.
- Verify white/pale rounded cards, evidence containers, side panels, and logic-chain nodes show a visible but subtle shadow in PowerPoint-rendered PNG previews.
- Verify evidence-led slides devote most of the available content area to the original paper evidence, with explanation text supporting it.
- Search generated scripts and PPTX text for `????`, mojibake, and other encoding-loss artifacts before delivery.
- Check page numbers and section navigation.
- Confirm source files were not modified.
