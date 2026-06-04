# Style System

This style is based on the user's preferred reference A: a polished Chinese academic competition deck about green finance and carbon reduction. It is formal, decorative, contest-oriented, and evidence-heavy.

## Visual Identity

- **Mood:** academic contest, green finance, refined policy research, high-stakes defense.
- **Base:** white content panels over teal atmospheric backgrounds.
- **Chrome:** top section navigation, bottom wave band, subtle teal gradients, gold accents.
- **Avoid:** generic consulting layouts, Swiss minimalism, magazine hero pages, plain Office templates.

## Style Priority

Use this order:

1. New template/reference style explicitly provided by the user.
2. Explicit user style instructions.
3. Default competition-frame style in this file.
4. Ordinary courseware mode, only when explicitly requested.

When a new template is active, use this file as a fallback for research readability, editable evidence, and competition-frame discipline.

## Frame Modes

### Default: Competition-Frame Mode

Use this unless the user explicitly requests ordinary courseware.

Required frame components:

- **Independent navigation bar:** top chapter tabs such as `研究背景 | 理论假设 | 研究设计 | 实证分析 | 机制检验 | 结论建议`, with the current chapter highlighted in gold or white.
- **Background identity:** cover/chapter pages use deep teal atmospheric backgrounds; content pages use white cards plus teal header/footer chrome.
- **Logic-chain breadcrumb:** long decks should show the current step in the causal/research chain, e.g. `政策冲击 -> 机制路径 -> 结果变量 -> 结论建议`.
- **Page marker:** include page number or section marker in a quiet corner.
- **Chapter rhythm:** insert a chapter divider, stage recap, or logic-chain return page every 8-12 slides in 50-70 slide decks.

### Optional: Ordinary Courseware Mode

Use only when the user explicitly asks for ordinary courseware or says not to use competition mode.

Allowed simplifications:

- Use lighter white/green course pages with minimal decoration.
- Replace top competition tabs with a simple header title and page number.
- Use fewer chapter dividers.
- Keep formula/table pages more lecture-like, but preserve claim/proof/takeaway structure.

Do not enter courseware mode merely because the deck is long. Long paper reports still default to competition-frame mode.

## Color Tokens

Use these defaults unless a new template overrides them:

| Role | Hex | Use |
|---|---:|---|
| Deep teal | `#065758` | Main chrome, headers, section badges, shadows |
| Teal dark | `#0A3F40` | Dark gradients, footer wave depth |
| Soft teal | `#61A298` | Secondary fills, connectors, diagram nodes |
| Gold | `#FFC819` | Active nav tab, key numbers, section highlights |
| Warm gold | `#F2CB88` | Title gradient accents, callout fills |
| Orange gold | `#E8A532` | Warning/contrast marks, rank emphasis |
| White | `#FFFFFF` | Cards and content panels |
| Ink | `#0F1115` | Body text |
| Pale teal | `#EAF5F2` | Light panel background |

Use teal as the dominant color and gold as a controlled accent. Do not introduce unrelated colors except when preserving a source figure or following an active template.

## Typography

Preferred font logic unless a new template overrides it:

- **Cover/title:** `思源宋体 CN Heavy`, `SimSun`, `Songti SC`, or a heavy Song-style fallback.
- **Section characters:** calligraphic or heavy serif style when available, but keep readable.
- **Body:** `思源黑体 CN Regular`, `Microsoft YaHei UI`, `SimHei`, or similar Chinese sans.
- **Numbers/equations:** Times New Roman or Cambria Math for equations; sans for labels.

Suggested sizes for 16:9 slides:

| Element | Size |
|---|---:|
| Cover title | 34-44 pt |
| Page claim/title | 24-34 pt |
| Section glyphs | 40-54 pt |
| Body text | 14-20 pt |
| Table text | 9-13 pt, but crop/split if unreadable |
| Labels/nav | 10-14 pt |

## Layout Grammar

- Use a 16:9 canvas unless the provided template uses a different ratio and the user wants to preserve it.
- Reserve the top 8-12% for navigation/header chrome on content slides.
- Reserve the bottom 8-12% for wave/footer chrome.
- Main content should sit in one or more white/semitransparent cards with rounded corners only when matching the reference.
- Use teal outlines, soft shadows, and gold active tabs to guide attention.
- Equations and regression tables should sit in clean white panels with a short result interpretation next to them.

## Competition Logic Chain

For empirical papers, build a visible argument chain and reuse it across the deck:

`现实问题 -> 文献缺口 -> 理论机制 -> 研究假设 -> 识别策略 -> 数据变量 -> 实证结果 -> 稳健性 -> 机制/异质性 -> 结论建议`

Implementation rules:

- Use a full logic-chain page near the beginning.
- Use small breadcrumbs on technical pages to show the current segment.
- Add a stage recap after dense formula/model sections.
- Return to the full chain before conclusion/policy pages.
- In 50-70 slide decks, never let more than 12 consecutive slides pass without a navigation, recap, or logic-chain cue.

## Reference A Motifs

Reuse these motifs when no new template is active:

- Full-width teal cover with blurred landscape/research imagery.
- Top navigation tabs: `研究背景 | 理论假设 | 实证分析 | 结论建议`.
- Left-side or top-left large Chinese section characters, e.g. `研究背景`, broken into decorative glyph blocks when needed.
- Bottom wave band in teal with light transparency.
- Gold badge for the active section.
- White rounded rectangles for explanations, formulas, and findings.
- Mechanism pages with teal node labels and arrows.
- Conclusion pages with three or four vertical evidence cards.

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
- Top navigation tabs should be visually full and readable. Prefer Chinese tab labels at 12-14 pt; reduce tiny decorative English header text when it competes with the tabs.
- Body text should normally be 16-18 pt on content pages. Use 14-15 pt only for secondary notes and side callouts. Do not shrink dense pages to fit; split them.
- Use full mechanism or research logic chains only on opening roadmap pages, section transition pages, stage recap pages, and conclusion synthesis pages.
- Technical content pages should show position through active top navigation, page marker, or a compact breadcrumb, not through a repeated full-width bottom logic chain.
- Use lightly rounded rectangles for cards, side panels, figure containers, callouts, and navigation tabs. Avoid sharp blocky rectangles unless showing the original paper's own table or figure.
- Add subtle shadows to white or no-fill cards and figure containers. Use restrained teal/gold gradients on covers, dividers, accent bands, and major callouts; do not apply decorative effects to the original evidence itself.

## Updated Layout Safety, Logic Chain, And Encoding Rules

These rules override any older wording in this reference.

- Treat the slide as fixed vertical zones: header/navigation, title, accent bar, optional kicker badge, content cards, footer chrome. A kicker badge must not sit on top of a content card or cover body text.
- Leave a visible gap between the gold title accent bar and the first card. If the title is long, lower the content region or split the slide.
- White and pale rounded cards, side panels, evidence containers, and logic-chain nodes should use restrained shadows. Prefer PowerPoint-native shadows through COM post-processing when python-pptx output is too flat.
- Use only one full logic-chain page by default. That page should be designed around the chain: full-width chain in the middle, short claim above, concise explanation cards below. Do not place the chain over ordinary text boxes.
- Other pages should not show the full chain. Use only the top navigation highlight, page marker, and optional compact section label.
- Generated scripts that contain Chinese must be written as UTF-8 files, or receive Chinese from UTF-8 JSON/text data. Avoid passing Chinese through PowerShell here-strings or shell pipes that may silently convert it to `????`.
- Before delivery, scan generated scripts and PPTX text for `????`, `鈥`, `鐮`, `瀹`, or other mojibake. Any such text in user-facing content must be fixed and the deck regenerated.
