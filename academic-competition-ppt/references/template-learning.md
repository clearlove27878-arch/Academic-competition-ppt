# Template Learning

Use this when the user provides a new PPT/PPTX, slide template, screenshot set, image reference, or says "follow this style".

## Trigger Phrases

Examples:

- "按这个风格来"
- "学习这个模板"
- "参考这个 PPT"
- "就照这个排版"
- "用这套风格做"
- "我给你一个新的模板"

## Workflow

1. **Confirm reference availability.** If a PPT/PPTX path is provided, verify it can be read. If only screenshots/images are provided, treat them as partial style references.
2. **Render and inspect.** Export slide previews/contact sheets when possible. Do not modify the reference file.
3. **Extract structure.** Identify page ratio, slide count, section rhythm, page types, repeated chrome, cover, chapter, body, figure/table, and closing patterns.
4. **Extract visual system.** Capture dominant colors, accent colors, fonts, title hierarchy, card style, background style, icons, navigation, dividers, and footer/header behavior.
5. **Assess research fit.** Decide which reference elements are safe for equations, regression tables, original figures, long text, and 50-70 slide decks.
6. **Produce a Template Style Brief.** Use `style-brief-format.md`. Present risks and recommended transfer strategy before building.
7. **Map paper to style.** Paper structure and evidence remain primary. Use the template for visual treatment and page rhythm.
8. **QA transfer.** Use `template-transfer-checklist.md` in addition to the normal quality checklist.

## Reference Type Rules

### Complete PPT/PPTX

- Prefer extracting a full page-type library.
- Use contact sheets to learn rhythm.
- If the deck is itself a template and the user wants strict following, preserve its skeleton as much as possible.
- If the deck is a loose reference, borrow the system rather than cloning every page.

### Few Screenshots Or Images

- Extract only visible style elements.
- Do not invent a full page-type library from 1-3 images.
- Ask for more references only if the missing style choice would materially change the output.

### Low-Quality Or Incompatible Template

Flag risks when:

- Tables or formulas would become unreadable.
- The style relies on non-editable full-slide screenshots.
- Fonts are unavailable and have no good fallback.
- The template has too little content capacity for a long paper.

When risks exist, recommend a hybrid: preserve cover/chapter/color identity, but use research-safe content pages.

## Transfer Priority

Use this order when conflicts occur:

1. Research accuracy and original evidence readability.
2. Paper structure and user's requested page count.
3. Active template visual identity.
4. Default competition-frame rules.

Do not sacrifice formulas, regression tables, or original figures just to mimic a decorative reference.

## Generated Backgrounds

If the active template has a clear background style, GPT Image prompts should follow it. Use generated images only for:

- Cover pages.
- Chapter dividers.
- Transition pages.
- Non-evidence atmospheric backgrounds.

Do not generate or redraw empirical figures unless the user explicitly asks and the distinction is documented.
