---
name: academic-competition-ppt
description: Create polished editable long-form Chinese academic paper presentation PPTX decks from papers, theses, reports, empirical research drafts, research plans, literature seminar materials, or style references. Use for long-form Chinese academic paper presentation, paper explanation deck, thesis/report/research-paper PPT, literature seminar, empirical economics/finance/management/management science research, identification strategies, mechanism tests, heterogeneity, robustness, coefficient interpretation, policy implications, and making a paper understandable rather than merely summarized.
---

# Academic Competition PPT

Build editable Chinese long-form paper presentation PPTX decks that make a real paper understandable. The default is not a short summary, roadshow, outline deck, or visual poster. Default output explains the paper's problem chain, concept chain, identification chain, result chain, original arguments, formulas, tables, and boundaries with enough pages for the audience to follow.

Always use this skill with the `Presentations` skill for PPTX output.

## 0. Highest Priority Generation Principles

Default decks are long-form paper overview / real paper presentation decks, not short summaries and not mechanical page expansion. A successful deck must be both intellectually explanatory and visually complete.

Long-form mode must satisfy all three:

- **Thicker content:** use more original paper ideas, source anchors, faithful paraphrases, and explanatory paragraphs.
- **Fuller layouts:** reduce meaningless blank space and preserve academic presentation density.
- **Stable visuals:** use the default refined teal academic style: white/pale-gray content pages, deep-teal top navigation, yellow active-section chips, readable inactive chips, light cards/formula panels, visible bottom or corner chrome, restrained gradients, and academic decoration.

Visual baseline rule / 视觉基准规则:

- The current refined deep-teal navigation version is the visual and layout baseline.
- Stronger competition chrome is folded into the default style as an optional treatment: bottom/corner chrome, deep-teal title bars, and more visible but still restrained background decoration.
- The later sparse long-form version is only a reference for problem-chain / concept-chain / identification-chain / result-chain decomposition.
- If a content-expansion reference mentions the earlier green version as a visual baseline, treat that wording as historical and use `references/style-system.md` plus `references/style_01_default_academic.md` for the current visual default.
- Do not inherit the later sparse version's small fonts, weak navigation, large empty areas, low decoration, missing bottom bars, title bloat, or mechanical split-page rhythm.

Every generated slide must feel like a designed paper explanation page: source-driven content, readable hierarchy, stable navigation, visible background/chrome, and a bottom takeaway unless it is a cover or chapter divider.

## 1. Mode And Reference Routing

- **Default:** Long-form Paper Presentation Mode / 长页数论文汇报模式.
- **Do not compress by default. 默认不压缩。** Prioritize complete paper narrative, sufficient logic-chain development, clear method explanation, and faithful reconstruction of the source paper's ideas.
- Default page ranges:
  - Ordinary paper presentation: 30-45 slides.
  - Empirical paper deep explanation: 40-60 slides.
  - Method-complex, formula-complex, or literature-seminar deck: 50-70 slides.
  - Research plan that should feel like a real paper presentation: 28-45 slides.
- **Short / summary variants** are allowed only when the user explicitly asks for "控制在15页以内", "少字版", "简洁版", "路演版", "答辩速览版", or similar.
- **Courseware:** only if the user explicitly asks for ordinary classroom/courseware style.
- **Reference priority:** explicit user template/reference/style request affects visual treatment > default long-form paper explanation > explicit short/courseware variant.
- When a new reference PPT/screenshot/template is provided, read `references/template-learning.md`, write a Template Style Brief, then use it unless it harms formulas, tables, evidence readability, or long-form paper explanation.

## 1A. Style Extension Mode / 风格拓展模式

Default behavior remains independent from imported templates. Visual templates affect appearance, not the default content paradigm: even with a selected template, the deck still defaults to long-form paper explanation unless the user explicitly asks for a short/roadshow version.

Enable the style extension library only when the user says things like:

- "使用某某模板风格", "参考我导入的模板", "按这个模板风格来";
- "换成科技蓝 / 红金 / 绿色发展 / 极简白 / 深色科技风";
- "给我几个PPT视觉风格选择";
- "从模板库里选一个适合这个主题的风格";
- provides a new PPTX/template/screenshot as a style source.

When style extension mode is active:

1. Read `references/style_catalog.md` first.
2. Select the style card that best matches the content theme, discipline, report type, audience, and user preference.
3. Read only the selected `references/style_*.md` card unless comparison among styles is requested.
4. Treat imported templates as visual references, not page-content sources. Do not mechanically copy template text, examples, logos, or decorative content.
5. If a style card conflicts with academic clarity, evidence readability, formula/table legibility, or factual discipline, the default long-form paper rules win unless the user explicitly accepts that tradeoff.
6. Do not reduce information completeness for design effect unless the user explicitly asks for a "简洁版", "路演版", "少字版", or similar lower-density output.

For new template PPTX imports, create or update a style card instead of changing the default style: place the source PPTX in `assets/templates/`, put key screenshots/contact sheets in `assets/screenshots/`, generate a draft style card in `references/`, and register it in `references/style_catalog.md`.

## 2. Source Decomposition

Extract and preserve the paper's full explanation chain:

`problem chain -> concept chain -> literature gap -> theory/mechanism -> hypotheses -> data/variables -> measurement logic -> identification/model -> coefficient interpretation -> baseline results or expected tests -> mechanism -> heterogeneity -> robustness/endogeneity -> contribution -> policy/method implications -> limitations/Q&A`

Default to deep reading rather than section compression:

- Read `references/paper-reading-protocol.md` to identify the problem, concept, identification, and result chains.
- Read `references/source-selection-rules.md` to classify original text into anchors, technical text, background text, and low-value text.
- Read `references/original-text-integration.md` to ensure each major chapter and each page is driven by source ideas rather than generic framework language.
- Use `references/paper-decomposition.md` for existing paper maps, figure/table maps, and slide inventory rules.
- For research plans, keep "planned test", "expected direction", and "to be estimated" language. Do not convert design sections into finished empirical findings.

## 3. Slide Narrative Contract

Every slide needs:

- one **question or claim**;
- one **audience cognition task**: understand a concept, variable, model, result, mechanism, boundary, or transition;
- one **plain-language explanation**;
- one **logical position**: what this slide inherits from the previous slide and what question it opens next;
- one **paper object**: model, formula, variable, figure, table, hypothesis, empirical test, source quote/anchor, policy scenario, or verified fact;
- one **source anchor or faithful paraphrase** on core pages, especially research question, definitions, variables, model, results, contribution, and policy implication.

Default slide copy is not pure bullets and not copied paragraphs. Use `references/slide-copywriting.md` and `references/title-compression-rules.md`: a compressed main title, an explanatory subtitle, 1-2 source-driven short paragraphs, 2-4 keywords, one inspectable paper object, and one bottom takeaway.

## 4. Long-Form Expansion And Page Types

Build slides by cognitive load, not by mechanically assigning one slide per paper heading.

- Read `references/narrative-expansion.md` when expanding a short outline into a long paper explanation.
- Read `references/logic-chain-patterns.md` for "follow-up question -> answer -> next follow-up question" pacing and long-form transition pages.
- Read `references/long-deck-page-types.md` for micro page types. Use multiple page types across a long deck; every 6-8 pages should vary rhythm through a transition, recap, evidence close-up, formula breakdown, or synthesis page.
- Read `references/long-deck-layout-rhythm.md` to prevent repeated card grids, mechanical split pages, and weak chapter rhythm.
- Read `references/page-types.md` when detailed layout choices are needed, especially for cover, navigation, evidence, model, variable, robustness, and Q&A pages.

Common long-form page types include reality paradox, question transition, literature gap, concept definition, variable measurement, mechanism path, formula breakdown, coefficient interpretation, identification threat, result explanation, mechanism test, heterogeneity story, robustness rebuttal, contribution, policy implication, method insight, limitation, and Q&A.

## 5. Formula, Results, Layout, And Visual Defaults

- Formula/model pages must explain: what question the model answers, what each key variable means, how the key coefficient is interpreted, what fixed effects/controls/identification design exclude, and what the model cannot answer. Read `references/formula-model-explanation.md` for complex methods.
- Result pages must answer the preceding question, not merely paste a table. Use `references/results-interpretation.md`: page question -> table/figure/key value -> result translation -> theory return -> next follow-up question.
- When content is dense, split pages before shrinking text. Read `references/layout-compatibility.md` for table, formula, chart, screenshot, and evidence layout tradeoffs.
- Read `references/visual-density-rules.md`, `references/navigation-system.md`, and `references/bottom-bar-and-background.md` before building the visual system. These rules are blocking defaults, not optional polish.
- Preserve the academic frame: navigation, chapter rhythm, evidence pages, model pages, variable pages, robustness pages, mechanism pages, conclusion pages, and PPTX editability.
- Keep body text readable. Do not solve overflow by shrinking text below readable thresholds.
- Preserve aspect ratio for screenshots, formulas, charts, and source figures. Never stretch both width and height.
- Keep the top navigation visible, clear, chapter-aware, and visually full. The left short title should usually be 16-20 pt; active chapter chips 12-16 pt; inactive chips 10-14 pt and about 2 pt smaller than active. The active section should be obvious without overpowering the slide title.
- Read `references/style-system.md`, `references/style_catalog.md`, the selected `references/style_*.md` card, `references/reference-a-observations.md`, `references/reference-light-agri-navigation.md`, and `references/evidence-image-handling.md` only when their detail is needed.

## 6. Font System / 中文字体系统

Use the font system to support long-form paper explanation: readability first, then academic title presence, then style-specific decoration.

- Default Chinese title skeleton: **思源宋体 CN Heavy** for cover titles, chapter titles, page-level titles, and formal navigation labels when available.
- Navigation defaults to 思源宋体 CN Heavy or the same Source Han Serif family: left short title about 16-20 pt; active chapter chip about 12-16 pt; inactive chip about 10-14 pt and usually 2 pt smaller than active. Active is bold, dark or yellow-chip highlighted, slightly stronger, and may use an underline; inactive is smaller dark gray/deep teal but still readable. Do not use decorative fonts in navigation.
- Body paragraphs use readable Chinese sans fonts: Source Han Sans SC / Noto Sans CJK SC / Microsoft YaHei fallback. Do not use Heavy Song/serif weight for long body text.
- Tables, data labels, page numbers, footnotes, and captions use sans fonts for small-size readability. Do not use decorative fonts there.
- English paper titles, subtitles, journal information, references, and English citations use Times New Roman by default. Chart numbers, data labels, and page numbers may use sans fonts for readability.
- Formulas do not require forced font replacement. Preserve source formula fonts when possible; use Times New Roman / Cambria Math only when safe. Complex formulas should use a clean screenshot plus editable explanation box if font replacement risks errors.
- **053-上首逸飞体** and **演示流动云楷** are local style accents only. Use them only according to style and page-type rules, never for body paragraphs, tables, formulas, footnotes, references, or dense explanations.
- If a font is missing or not licensed for embedding/distribution, use fallback fonts and continue. Font choice must never cause PPT corruption, Chinese mojibake, missing glyphs, formula errors, unreadable tables, or interrupted generation.

Read `references/font_registry.md` before packaging or embedding fonts, and read `references/font_usage_rules.md` when assigning fonts by page role, style, or text function.

## 7. Fact, Policy, And Causal Discipline

- Do not invent empirical results, event dates, policy shocks, regression outcomes, sample sizes, or company facts.
- If facts may have changed or come from official/current sources, verify them before using them.
- For official product limits, pricing, model specs, and API rules, prefer official documentation.
- For reports/user feedback, label them as reports or feedback, not official announcements.
- Policy suggestions should be cautious and general unless the source paper has stronger evidence.
- Do not claim government intervention has produced causal effects without a clear policy event and valid design.
- Do not add DID/DDD as the current main method unless the paper or facts provide a clear treatment group, timing, and identification basis.
- Preserve statements such as "prediction model", "counterfactual scenario", "research design", "proposed test", or "expected direction" when results are not yet established.

## 8. Compatibility Rules

- **Chinese encoding:** treat Chinese as data, not shell source. Put slide copy in UTF-8 `.json`, `.md`, or `.txt`; read with explicit UTF-8. Avoid PowerShell here-strings, shell pipes, command arguments, or inline JS/Python containing Chinese deck copy.
- If any generated source, preview, inventory, QA note, or PPT visible text contains `????`, mojibake, or replacement characters, regenerate from clean UTF-8 instead of patching corrupted text.
- **Formula fallback:** for Word/OMML or complex math, first try clear editable/typeset formulas. If there is mojibake, missing symbols, broken superscripts/subscripts, font substitution, or blur, crop the original source formula and embed it as a high-resolution image.
- Formula screenshots should include only the equation body and needed number, preserve aspect ratio, sit in a white formula panel, and be paired with editable symbol/economic meaning.
- Prefer editable research content; use raster only for source figures, formulas, screenshots, complex backgrounds, and cropped evidence.

## 9. Build Workflow

1. Read source paper/report/research plan and any reference/template.
2. Build the problem chain, concept chain, identification chain, and result chain.
3. Mark source text as original anchors, technical original text, background original text, or low-value text.
4. Build a claim spine and slide inventory before creating slides.
5. Choose the default long-form page count unless the user explicitly requests a short/summary variant.
6. Expand chapters into explanation units by cognitive load: concept, model, formula step, variable, evidence, doubt, result, mechanism, boundary, or transition.
7. Select page type/layout for each unit.
8. Generate editable PPTX using Presentations/artifact-tool.
9. Render previews/contact sheet and inspect weak pages.
10. Iterate layout, evidence scale, text fit, formula clarity, navigation, and page rhythm.
11. Export final PPTX only after QA passes.

## 10. QA Gate

Before delivery:

- Render PNG previews or a contact sheet.
- Check Chinese visible text with `scripts/pptx_visible_text_qa.py <final.pptx>` and report the result.
- Run the long-form paper deck audit in `references/qa-long-paper-deck.md`.
- Run the visual long-deck audit in `references/qa-visual-long-deck.md`.
- Run the font QA in `references/font_usage_rules.md`: title, navigation, body, table, formula, page number, footnote, English text, fallback, and decorative-font usage.
- Verify problem chain, concept chain, identification chain, and result chain are all represented.
- Verify source anchors appear on core pages and source ideas are faithfully paraphrased.
- Verify formulas explain economic meaning and model boundaries.
- Verify result pages answer the question they were designed to answer.
- Verify research plans do not invent completed results.
- Check top navigation, bottom takeaway bars, page numbers, background decoration, visual density, title length, layout rhythm, no overlaps, no stretched evidence, no unreadable tables, no excessive blank space, no repeated card-grid monotony, no font substitution damage, and no text overflow caused by font changes.
- Deliver final editable PPTX, preview/contact sheet, slide inventory, QA notes, and any placeholder notes.

## 11. Hard Rules

- Do not mutate the user's source paper or reference/template deck.
- Do not default to short summary decks.
- Do not mechanically expand pages without adding original paper substance and visual density.
- Do not reduce a research paper to section-title slides.
- Do not turn complex concepts into one-line bullets when explanation is needed.
- Do not let generic framework phrases replace the paper's own ideas.
- Do not use main titles longer than 18 Chinese characters; split into short title + subtitle.
- Do not omit the top navigation or bottom takeaway bar on ordinary content pages.
- Do not use isolated repeated `▶ ▶` symbols without an integrated navigation/header design.
- Do not leave large pure-white empty backgrounds; use subtle academic decoration.
- Do not show formulas without explaining economic meaning.
- Do not show regression tables or expected tests without saying what question they answer.
- Do not invent empirical results when the source is only a research plan.
- Do not sacrifice long-form paper explanation for visual minimalism.
- Do not repeat the same card-grid layout across a long deck.
- Do not use decorative fonts as body, table, formula, navigation, footnote, or reference fonts.
- Do not use Heavy Song/serif title fonts for long body paragraphs.
- Do not embed or redistribute commercial, system, member-only, or license-unclear fonts by default.
- Do not drop the academic/competition frame unless explicitly requested.
- Do not make evidence a decorative thumbnail; evidence should be inspectable.
- Do not reduce regression/table/formula text below readable thresholds; split or crop instead.
- Do not allow kicker labels, title bars, card outlines, or text boxes to overlap.
- Do not deliver a PPTX with visible Chinese encoding damage.
- Do not use the guizang magazine/Swiss HTML style unless explicitly requested.
