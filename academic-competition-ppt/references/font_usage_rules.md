# Font Usage Rules

Use this file when assigning fonts by page hierarchy, style, and text function. The font system serves long-form paper explanation; readability and correctness win over decoration.

## Default Font Hierarchy

1. **Cover Chinese main title:** 思源宋体 CN Heavy, large and formal.
2. **Chapter transition Chinese title:** 思源宋体 CN Heavy.
3. **Page-level title:** 思源宋体 CN Heavy, smaller than cover/chapter titles.
4. **Top navigation:** all nav labels use 思源宋体 CN Heavy or same Source Han Serif family. The left short title is about 16-20 pt; active chapter chips are about 12-16 pt; inactive chips are about 10-14 pt and usually 2 pt smaller than active. Active is bold and visually anchored by yellow chip, deep-teal treatment, short underline, or soft highlight; inactive remains deep teal/dark gray and readable. Never use decorative fonts or mixed font families in navigation.
5. **Body paragraphs:** Source Han Sans SC / Noto Sans CJK SC / Microsoft YaHei fallback. Avoid Heavy Song/serif for long text.
6. **Tables, data labels, page numbers, footnotes:** sans fonts for small-size readability.
7. **English titles, subtitles, paper information, journals, references, English quotes:** Times New Roman by default.
8. **Formulas:** preserve original font; use Times New Roman / Cambria Math only when safe; screenshot complex formulas if font replacement risks errors.

## Size Floor For 16:9 Slides

- Main title: 30-40 pt.
- Chapter title: 36-48 pt.
- Subtitle/guide sentence: 18-24 pt.
- Body paragraphs: 16-20 pt.
- Card body: 14-17 pt.
- Table body: 11-14 pt.
- Left short navigation title: about 16-20 pt.
- Active chapter navigation chip: about 12-16 pt.
- Inactive chapter navigation chip: about 10-14 pt, usually 2 pt below active.
- Footnote/source: 8-10 pt.
- Content below 10 pt cannot carry core information.

## Page-Type Matching

- Cover page: 思源宋体 CN Heavy + Times New Roman.
- Contents page: first-level items use 思源宋体; explanatory text uses sans.
- Chapter transition page: 思源宋体 CN Heavy; special styles may add one small decorative accent.
- Question transition page: title uses 思源宋体; short follow-up phrase may use a decorative accent only if style-appropriate.
- Concept explanation page: title uses 思源宋体; body uses sans.
- Formula/model page: title uses 思源宋体; formula keeps original font; explanation uses sans.
- Table/result page: title uses 思源宋体; table, numbers, captions, and notes use sans.
- Robustness/identification page: avoid decorative fonts; keep serious title + sans explanation.
- Policy implication/research insight page: use 思源宋体 to strengthen formal tone; decorative accents only if they do not weaken academic seriousness.
- Q&A page: Chinese main title uses 思源宋体; English `Q&A` may use Times New Roman.

## Decorative Font Rules

### 053-上首逸飞体

Use only for tech, hardcore, dark-tech, data-governance, AI, digital economy, or similar visual styles.

Allowed:

- secondary titles;
- small card titles;
- keyword labels;
- chapter numbers;
- conclusion emphasis words;
- short tech-guide phrases.

Limits:

- Do not use for body paragraphs, tables, formula explanations, footnotes, references, or navigation.
- At most 1-3 uses per slide.
- Each use should usually be 2-8 Chinese characters.
- Do not use across multiple consecutive lines.
- If readability drops, fall back to 思源宋体 or sans.

### 演示流动云楷

Use only for ink, humanities/social-science, ecological-civilization poetic, or calm cultural styles.

Allowed:

- short quotes;
- guide phrases;
- secondary titles;
- small card titles;
- chapter-page short lines;
- research-insight keywords.

Limits:

- Do not use for body text, model pages, variable tables, regression result pages, formula pages, data-source pages, or serious identification-strategy pages.
- At most 1-2 uses per slide.
- It must not carry long-form reading load.
- If the slide is a formal paper explanation page, prefer 思源宋体.

## Font QA

Before delivery, check:

- Cover, chapter, page titles use the correct title role.
- Navigation uses formal serif/title font or approved fallback; active/inactive hierarchy remains stable.
- Navigation labels use a single Source Han Serif family; left short title is about 16-20 pt, active chapter chips are about 12-16 pt, and inactive chips are about 10-14 pt when space allows.
- Body paragraphs do not use decorative fonts or Heavy title fonts.
- Tables, labels, page numbers, footnotes, and captions use readable sans fonts.
- English paper information and references use Times New Roman or fallback.
- Formulas preserve original meaning and do not break due to font replacement.
- Decorative fonts are limited by style, page type, frequency, and character count.
- Missing fonts fall back without Chinese glyph loss, layout overflow, or PPT corruption.
- Exported previews show no font substitution damage, overlap, clipping, mojibake, or unreadable small text.
