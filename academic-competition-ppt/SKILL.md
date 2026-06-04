---
name: academic-competition-ppt
description: Create polished editable Chinese academic competition PowerPoint decks from papers, theses, empirical research drafts, PPT outlines, or user-provided style references. Use when Codex needs to parse a Chinese academic paper and generate an academic/contest-style PPTX deck, especially for energy economics, green finance, environmental regulation, DID/PSM-DID/regression studies, mechanism tests, heterogeneity analysis, policy recommendations, or requests to follow a supplied PPT/template/screenshot style.
---

# Academic Competition PPT

Generate editable PowerPoint decks for Chinese academic competitions, thesis-style defenses, and long-form paper reports. The default visual system is the user's preferred "strictly like reference A" style: deep teal, gold accents, white research cards, top section navigation, bottom wave chrome, Song-style heavy titles, and dense but legible empirical evidence pages. For 40-page-plus papers, support 50-70 slide decks that explain every model, variable, table, robustness check, and mechanism in detail while still keeping a competition-style framework. When the user supplies a new template, PPT, screenshot, or says to follow a specific style, learn that reference first and produce a Template Style Brief before building.

Use this skill with the `Presentations` skill whenever the output is a PPTX. Do not create a generic business deck, Swiss webpage deck, or magazine-style HTML deck unless the user explicitly asks for a different medium.

## Mode Router

Default to **competition-frame mode** for both short and long decks. In this mode, even a 50-70 slide report must keep independent navigation, chapter dividers, visual background/chrome, and periodic logic-chain return pages. Do not put the full mechanism or logic chain on every slide; preserve technical page space for evidence and explanation.

Switch to **ordinary courseware mode** only when the user explicitly asks for a non-competition, ordinary classroom, or lecture-style courseware deck. Courseware mode may use lighter backgrounds and simpler headers, but should still preserve clear structure and readability.

When the user explicitly provides a new style reference, use this priority:

`new template/reference style > explicit user style instructions > default competition-frame style > ordinary courseware mode`

Template learning is task-local by default. Do not permanently replace the default style unless the user explicitly asks to make the new style the default.

## Workflow

1. **Learn any provided template/reference style first.** If the user provides a PPT/PPTX, screenshots, images, or says "follow this style", read `references/template-learning.md`, extract a Template Style Brief, and use it as the active style unless it harms readability or research integrity.
2. **Read the source paper.** Extract the title, research question, theoretical logic, hypotheses, model, variables, sample period, identification strategy, tables/figures, main findings, robustness checks, mechanism tests, heterogeneity results, conclusions, and policy implications.
3. **Write a claim spine before building slides.** Each page needs one claim and one proof object. Avoid making pages that only restate section names.
4. **Choose a page count mode.** Use 15-20 slides for competition summaries. Use 50-70 slides for long paper reports when the user wants every detail of a 40-page-plus paper covered. Unless the user explicitly requests ordinary courseware, keep the competition-frame mode.
5. **Load the needed references:**
   - Read `references/template-learning.md` when a new template, PPT, screenshot, or "follow this style" request is present.
   - Read `references/style-brief-format.md` before presenting the Template Style Brief.
   - Read `references/template-transfer-checklist.md` when QAing a deck generated from a new reference style.
   - Read `references/reference-a-observations.md` when you need the concrete observations extracted from the user's preferred reference deck.
   - Read `references/econometrics-longform-observations.md` when designing long 50-70 slide paper reports.
   - Read `references/paper-decomposition.md` when parsing a paper or deciding what evidence belongs on slides.
   - Read `references/evidence-image-handling.md` before importing original paper figures, tables, screenshots, or PDF crops.
   - Read `references/style-system.md` before designing any slide.
   - Read `references/page-types.md` before planning or generating the deck.
   - Read `references/quality-checklist.md` before final export.
6. **Map paper structure to the active style.** Paper logic and evidence remain primary; the template decides visual treatment, page rhythm, and component style.
7. **Build editable PPTX slides.** Prefer text boxes, native tables, shapes, connectors, and image placeholders. Use rasterized background elements only for complex texture/wave chrome. Keep user-editable research content editable. Treat original paper figures/tables as primary evidence objects: crop removable whitespace, preserve aspect ratio, and make the evidence region as large as the slide layout allows. Keep title, accent bar, kicker badges, cards, and evidence panels in separate vertical zones so they do not overlap.
8. **Apply PPT polish.** Prefer native PowerPoint shadows for white/no-fill rounded cards, side panels, evidence containers, navigation tabs, and logic-chain nodes. If a Python library cannot express the desired shadow reliably, use PowerPoint COM post-processing before final export.
9. **Render and QA.** Export slide previews/contact sheet, compare against the style rules and any Template Style Brief, then iterate the weakest pages before delivering. Specifically check that source figures are not stretched, navigation text is readable, content elements do not overlap, full logic-chain diagrams appear on only one dedicated page, and no Chinese text has degraded into question marks or mojibake.

## Deck Length Modes

### Competition Summary Mode: 15-20 Slides

Use when the user needs a contest/defense deck with high polish and compressed storytelling.

`Cover -> Hook/Question -> Background -> Literature -> Contribution -> Theory/Model -> Mechanism -> Research Design -> Variables/Data -> Baseline Regression -> Robustness -> Dynamic/Parallel Trend -> Mechanism Test -> Heterogeneity -> Integrated Mechanism -> Conclusions -> Policy Suggestions -> Thanks`

Expand to about 20 slides by splitting dense evidence pages, not by duplicating layouts. Common expansions: separate data/sample from variable definitions, split robustness into 2-3 methods, split mechanism and heterogeneity, or add a complete mechanism diagram.

### Long Paper Report Mode: 50-70 Slides

Use when the user provides a 40-page-plus paper and wants a detailed report. Preserve the paper's full logic instead of compressing aggressively, while keeping the competition framework:

`Cover -> Hook -> Table of Contents -> Background and Puzzle -> Theory Definitions -> Model/Formula Walkthrough -> Identification and Estimation -> Data/Sample/Variables -> Measurement Construction -> Main Results -> Extensions -> Robustness Battery -> Mechanisms -> Heterogeneity -> Limitations/Interpretation -> Conclusion -> Q&A`

Long mode should use many focused micro-slides: one formula step, one variable definition, one table column group, one plot interpretation, or one robustness test per slide. Add chapter dividers, stage recaps, and logic-chain return pages every 8-12 slides so the deck feels like a competition-grade long report, not a plain lecture file.

## Style Defaults

- Theme: deep teal academic contest style, not flat minimalism.
- Main colors: `#065758` deep teal, `#FFC819` gold, `#61A298` soft teal, white cards, dark text `#0F1115`.
- Typography: heavy Song-style Chinese titles; Hei/Sans body; use font fallbacks that work on Windows.
- Chrome: top nav bar with section tabs; bottom teal wave/gradient band; small competition label or page marker.
- Long-form competition frame: every content page should show where the audience is in the argument through top navigation, current module label, page marker, or concise breadcrumb. Use a full logic-chain diagram on one dedicated logic-chain page only unless the user explicitly asks for repeated recaps.
- Evidence: regression tables, equations, diagrams, and plots should be framed as research proof objects, never decorative filler.

## Hard Rules

- Do not mutate the user's source paper or reference PPT.
- Do not mutate a user-provided template/reference deck. Duplicate, inspect, render, or import it only as needed.
- Do not make every page a card grid. Vary page structure across at least 12 distinct page types in a 20-slide deck and at least 18 distinct micro-page patterns in a 50-70 slide deck.
- Do not invent empirical results. If the paper lacks a number/table/figure, mark a placeholder clearly.
- Do not use emoji as icons. Use simple academic icons, native shapes, or small pictograms.
- Do not reduce regression table text below readable thresholds; if a table is too dense, split or crop to the key columns.
- Do not distort source figures or screenshots by forcing both width and height. Use contain, smart-crop, or split-slide strategies to preserve aspect ratio.
- Do not leave large unused whitespace inside imported paper evidence. Crop safe white margins, PDF headers/footers, page numbers, and irrelevant notes, then scale the remaining figure/table to occupy the evidence panel.
- Do not make original paper evidence a small decorative thumbnail. On evidence-led slides, the paper figure/table should be the main visual object; explanatory text should support it, not compete with it.
- Do not allow kicker labels, title bars, card outlines, or text boxes to overlap. Leave explicit safety spacing or split the slide.
- Do not deliver a PPTX if generated Chinese text contains `????`, mojibake, or other encoding-loss artifacts.
- Do not drop the competition framework in long decks unless the user explicitly asks for ordinary courseware mode.
- Do not blindly clone a new template if it makes formulas, tables, original figures, or regression evidence unreadable. Preserve paper structure and readability first.
- Do not use the guizang magazine/Swiss HTML style unless explicitly requested. This skill's default is editable PPTX academic contest style.

## Output Contract

When building a deck, deliver:

- Final editable PPTX.
- Rendered PNG previews or a contact sheet for QA.
- A short slide inventory mapping page number to source evidence and page type.
- A Template Style Brief when a new reference style is provided.
- Notes on any placeholders caused by missing source data.
