# Style System

This file defines the default academic competition frame for long-form paper presentations. It is formal, evidence-heavy, and suitable for Chinese academic competitions, course reports, thesis defenses, literature seminars, and real paper explanation decks. Imported templates and catalog styles are optional visual extensions; they must not overwrite the default long-form paper explanation logic unless the user explicitly asks for a short/roadshow version.

## Visual Identity

- **Mood:** academic contest, policy research, thesis defense, refined evidence-heavy presentation.
- **Base:** clean white or pale-gray content pages with restrained teal/deep-green academic chrome.
- **Chrome:** deep-teal top navigation, yellow active-section chips, readable inactive chips, visible bottom or corner chrome, page marker, light cards/formula panels, controlled gold highlights, restrained low-opacity decoration, and optional deep-teal title bars on emphasis pages.
- **Avoid:** generic consulting layouts, Swiss minimalism, magazine hero pages, plain Office templates.
- **Visual baseline:** the current refined deep-teal navigation deck is the default baseline for density, navigation, bottom chrome, and background identity. Stronger competition chrome is available inside the same default style through bottom/corner chrome, deep-teal title bars, and more visible but restrained background decoration. Do not imitate sparse long-form drafts with weak navigation, tiny text, and large empty white space.

## Style Priority

Use this order:

1. New template/reference style explicitly provided by the user.
2. Explicit user style instructions.
3. Default academic long-form competition style in this file and `style_01_default_academic.md`.
4. Ordinary courseware mode, only when explicitly requested.

When a new template is active, use this file as a fallback for long-form paper explanation, research readability, editable evidence, and competition-frame discipline.

If a content-expansion reference still mentions the earlier green academic version as a visual baseline, treat that wording as a request for the default style's stronger-chrome treatment, not a separate style card.

## Frame Modes

### Default: Long-Form Competition-Frame Mode

Use this unless the user explicitly requests ordinary courseware, short summary, roadshow, or speed-defense mode.

Required frame components:

- **Independent navigation bar:** top chapter labels such as `研究背景 | 理论机制 | 研究设计 | 实证分析 | 稳健检验 | 结论建议`, adapted and compressed to the topic. All navigation labels use 思源宋体 CN Heavy or the same Source Han Serif family.
- **Independent navigation bar:** top navigation is a chapter positioning system and should occupy about 7%-10% of slide height when needed. Left short title is about 16-20 pt; active chapter chip is about 12-16 pt; inactive chip is about 10-14 pt and usually 2 pt smaller than active. Active is visually anchored by a yellow chip, deep-teal fill/text, bold weight, underline, or short color block; inactive remains deep teal/dark gray, readable, and visually lighter.
- **Background identity:** cover/chapter pages may use deep teal or restrained academic backgrounds; content pages use white/pale-gray panels, clean evidence containers, restrained teal/gold accents, and subtle high-transparency decoration.
- **Bottom takeaway bar:** ordinary content pages include a bottom bar or corner chrome with one page-specific conclusion, boundary, or transition. Low-saturation deep-teal, pale-teal, and pale-yellow gradients are allowed. It should close the slide visually without becoming a second navigation block.
- **Logic-chain breadcrumb:** long decks should show the current step in the causal/research chain, e.g. `政策冲击 -> 机制路径 -> 结果变量 -> 结论建议`.
- **Page marker:** include page number or section marker in a quiet corner.
- **Chapter rhythm:** insert a chapter divider, stage recap, or logic-chain return page every 6-8 slides in long paper decks.

### Optional: Ordinary Courseware Mode

Use only when the user explicitly asks for ordinary courseware or says not to use competition mode.

Allowed simplifications:

- Use lighter white/green course pages with minimal decoration.
- Replace top competition tabs with a simple header title and page number.
- Use fewer chapter dividers.
- Keep formula/table pages more lecture-like, but preserve claim/proof/takeaway structure.

Do not enter courseware mode merely because the deck is long. Long paper reports still default to long-form competition-frame mode.

## Color Tokens

Use these defaults unless a new template overrides them:

| Role | Hex | Use |
|---|---:|---|
| Deep teal | `#065758` | Main chrome, headers, title bars, section badges, shadows |
| Teal dark | `#0A3F40` | Dark gradients, cover overlays, footer or corner chrome |
| Soft teal | `#61A298` | Secondary fills, connectors, diagram nodes |
| Gold | `#FFC819` | Active nav, key numbers, emphasis words, section highlights |
| Warm gold | `#F2CB88` | Title gradient accents, callout fills |
| Orange gold | `#E8A532` | Warning/contrast marks, rank emphasis |
| White | `#FFFFFF` | Cards and content panels |
| Ink | `#0F1115` | Body text |
| Pale teal | `#EAF5F2` | Light panel background |

Use teal/deep green as the dominant identity color and gold as a controlled accent. Do not introduce unrelated colors except when preserving a source figure or following an active template.

## Typography

Preferred font logic unless a new template overrides it. Detailed role rules live in `font_registry.md` and `font_usage_rules.md`.

- **Cover/title/chapter/page title:** `思源宋体 CN Heavy` by default, with Source Han Serif / Noto Serif CJK / SimSun / Microsoft YaHei fallbacks.
- **Navigation:** `思源宋体 CN Heavy` or the same Source Han Serif family for every nav label. Left short title is about 16-20 pt; active chapter chip is about 12-16 pt; inactive chip is about 10-14 pt and usually 2 pt smaller than active. Active is bold and anchored by deep teal/yellow chip, short underline, or soft highlight; inactive is deep teal/dark gray, readable, and visually lighter. Do not use decorative fonts or sans/serif mixing in navigation.
- **Body:** Source Han Sans SC, Noto Sans CJK SC, Microsoft YaHei, SimHei, or similar Chinese sans. Do not use Heavy Song/serif for long body paragraphs.
- **Tables/labels/page numbers/footnotes:** Chinese sans for small-size readability.
- **English academic text:** Times New Roman for English paper titles, subtitles, journal information, references, and English citations.
- **Numbers/equations:** Preserve original formula fonts when possible; Times New Roman or Cambria Math only when safe; sans for data labels.
- **Decorative accents:** `053-上首逸飞体` only for local tech/hardcore accents; `演示流动云楷` only for local ink/humanities/ecological accents. Never use decorative fonts for body, tables, formulas, footnotes, references, or navigation.

Suggested sizes for 16:9 slides:

| Element | Size |
|---|---:|
| Cover title | 34-44 pt |
| Chapter title | 36-48 pt |
| Page title | 30-40 pt |
| Subtitle/guide | 18-24 pt |
| Body text | 16-20 pt |
| Card body | 14-17 pt |
| Table text | 11-14 pt, but crop/split if unreadable |
| Left short nav title | 16-20 pt |
| Active chapter nav chip | 12-16 pt |
| Inactive chapter nav chip | 10-14 pt, usually 2 pt below active |
| Footnote/source | 8-10 pt |

If a font is missing or not licensed for embedding, use the fallback stack and re-check text fit, glyph coverage, formula accuracy, and exported preview quality.

## Layout Grammar

- Use a 16:9 canvas unless the provided template uses a different ratio and the user wants to preserve it.
- Reserve the top 9-13% for title/navigation/header chrome on content slides when fuller navigation is needed; top navigation itself should feel like a real chapter system.
- Reserve the bottom 3-7% for a takeaway bar, footer note, restrained footer chrome, or corner chrome on ordinary content slides.
- Main content should sit in one or more white/semitransparent cards with rounded corners only when matching the reference.
- Use teal/deep-green outlines, deep-teal title bars, soft shadows, restrained gradients, and controlled gold accents to guide attention.
- Equations and regression tables should sit in clean white panels with a short result interpretation next to them.
- White or transparent rounded content cards may use low-contrast gradient fills, gradient-like layered edges, subtle shadows, or semi-transparent strokes instead of flat single-color borders.
- Gradients must be low-saturation and low-contrast; they should improve depth and polish, not lower body-text, table, or formula readability.
- Ordinary content slide visual fill should be about 65%-85%. If it is below 60%, add source-driven paragraph content, paper object, explanation panel, bottom takeaway, or subtle background decoration.
- Avoid pure white empty canvases. Use high-transparency pale green geometry, arcs, grids, bottom bands, corner abstract blocks, or slightly more visible background decoration that does not interfere with content.

## Competition Logic Chain

For empirical papers, build a visible argument chain and reuse it across the deck:

`现实问题 -> 文献缺口 -> 理论机制 -> 研究假设 -> 识别策略 -> 数据变量 -> 实证结果 -> 稳健性 -> 机制/异质性 -> 结论建议`

Implementation rules:

- Use a full logic-chain page near the beginning.
- Use small breadcrumbs on technical pages to show the current segment.
- Add a stage recap after dense formula/model sections.
- Return to the full chain before conclusion/policy pages.
- In long decks, never let more than 6-8 consecutive slides pass without a visual rhythm change, recap, or logic-chain cue.

## Stronger-Chrome Default Motifs

Use these deep-teal/gold motifs when the default style needs more competition weight, stronger bottom chrome, or a clearer academic frame:

- Full-width teal cover with blurred landscape/research imagery.
- Top navigation tabs: `研究背景 | 理论假设 | 实证分析 | 结论建议`.
- Left-side or top-left large Chinese section characters, e.g. `研究背景`, broken into decorative glyph blocks when needed.
- Bottom wave band or gradient bar in teal with light transparency.
- Gold/yellow badge for the active section.
- White rounded rectangles for explanations, formulas, and findings.
- Mechanism pages with teal node labels and arrows.
- Conclusion pages with three or four vertical evidence cards.

## Optional Light Agricultural Navigation Motifs

Use these motifs only when the user explicitly chooses the Green Fresh Pastoral / 绿色清新田园简约风 style, asks for a light agricultural or green fresh style, or provides the matching template. The full style card is `style_07_green_fresh_pastoral.md`.

- White or pale-gray content pages with subtle geometric background texture.
- Top-left lightweight double-triangle/arrow identity mark plus a large deep green page title.
- Top horizontal navigation with 思源宋体 labels: active chapter about 16 pt, bold, deep green, and optionally a short gradient/shadow underline; inactive chapters about 12 pt and black/dark gray.
- No bottom rectangular navigation block; use a thin divider line only.
- Keep any triangle/arrow mark integrated with the header; do not leave isolated repeated `▶ ▶` symbols as decoration.
- Ordinary content pages still need a bottom takeaway bar or equivalent footer chrome.
- Deep green rounded title pills, table headers, flow labels, and case labels may use subtle gradients or shadows for polish.
- Yellow highlights for selected keywords and numbers, used sparingly.
- Full-bleed agricultural/research photos mainly for cover, chapter divider, closing, case, and application pages.

## Original Figures And Generated Backgrounds

- Prioritize original figures, tables, mechanism charts, and regression outputs from the paper.
- Use the active template only to frame, crop, annotate, or explain original evidence.
- Generated background images may be used for covers, chapter dividers, and transition pages.
- Do not let generated backgrounds replace evidence figures or make formulas/tables harder to read.

## Native PPT Preference

Keep research content editable:

- Use native tables for simplified regression summaries.
- Use editable text boxes for claims and notes.
- Use native shapes/connectors for mechanisms and flow diagrams.
- Use image placeholders for original plots, complex regression screenshots, and maps.
- Use raster images only for decorative backgrounds, template textures, or imported source figures.

## Updated Figure, Readability, And Polish Rules

These rules override any older wording in this reference.

- Preserve aspect ratio for every source figure, table screenshot, formula screenshot, PDF crop, and other text-bearing image. Never force both width and height when that would stretch the source.
- Treat original paper figures/tables as the main proof object on evidence slides. They should be large enough to read from the audience view, not used as decorative thumbnails.
- Use `smart_crop` as the default for PDF evidence: remove obvious white margins, page numbers, watermarks, footers, and blank areas above/below tables. Do not crop axes, captions needed for meaning, table notes, significance stars, formula symbols, or panel labels.
- Use `wide_extract` when a PDF page contains a smaller figure/table that can be isolated cleanly. Expand the extracted object to fill most of the evidence panel while preserving its aspect ratio.
- Use `contain` only as a fallback when smart cropping is unsafe. If contain leaves large internal whitespace, try a safer crop or split the evidence into panels.
- If a figure/table is too small after aspect-ratio preservation, split it into focused panels or key-column slides instead of stretching it.
- Evidence-led slide balance: allocate about 55-70% of the usable content width to the original evidence image and about 25-40% to editable explanation. For full-table walkthroughs, allow the evidence image to take nearly the full content area and move explanation to a compact top/bottom callout.
- Cropping priority for paper evidence: keep the table/figure body first, keep panel labels and critical captions second, and remove PDF page furniture third. Long explanatory captions can be summarized in editable PPT text instead of consuming image space.
- If the original table remains unreadable after crop and scaling, create a pair of slides: one full-table context slide and one key-row/key-column close-up slide.
- Top navigation tabs should be visually full and readable. Prefer a left short title at 16-20 pt, active chapter chips at 12-16 pt, and inactive chips at 10-14 pt; reduce tiny decorative English header text when it competes with the tabs.
- Body text should normally be 16-18 pt on content pages. Use 14-15 pt only for secondary notes and side callouts. Do not shrink dense pages to fit; split them.
- Main titles should usually be 6-14 Chinese characters; titles over 18 Chinese characters must become short title + subtitle.
- Use full mechanism or research logic chains only on opening roadmap pages, section transition pages, stage recap pages, and conclusion synthesis pages.
- Technical content pages should show position through active top navigation, page marker, or a compact breadcrumb, not through a repeated full-width bottom logic chain.
- Use lightly rounded rectangles for cards, side panels, figure containers, callouts, and navigation tabs. Avoid sharp blocky rectangles unless showing the original paper's own table or figure.
- Add subtle shadows to white or no-fill cards and figure containers. Use restrained teal/gold gradients on covers, dividers, accent bands, bottom bars, navigation highlights, and major callouts; do not apply decorative effects to the original evidence itself.

## Updated Layout Safety, Logic Chain, And Encoding Rules

These rules override any older wording in this reference.

- Treat the slide as fixed vertical zones: header/navigation, title, accent bar, optional kicker badge, content cards, footer chrome. A kicker badge must not sit on top of a content card or cover body text.
- Leave a visible gap between the gold title accent bar and the first card. If the title is long, lower the content region or split the slide.
- White and pale rounded cards, side panels, evidence containers, and logic-chain nodes should use restrained shadows, soft gradient fills, gradient-like edge layers, or semi-transparent strokes. Prefer PowerPoint-native shadows through COM post-processing when python-pptx output is too flat.
- Use only one full logic-chain page by default. That page should be designed around the chain: full-width chain in the middle, short claim above, concise explanation cards below. Do not place the chain over ordinary text boxes.
- Other pages should not show the full chain. Use only the top navigation highlight, page marker, and optional compact section label.
- Generated scripts that contain Chinese must be written as UTF-8 files, or receive Chinese from UTF-8 JSON/text data. Avoid passing Chinese through PowerShell here-strings or shell pipes that may silently convert it to `????`.
- Before delivery, scan generated scripts and PPTX text for `????`, `鈥`, `鐮`, `瀹`, or other mojibake. Any such text in user-facing content must be fixed and the deck regenerated.
