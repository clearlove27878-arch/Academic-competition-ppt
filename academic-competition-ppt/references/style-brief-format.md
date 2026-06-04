# Template Style Brief Format

When a new style reference is provided, present a concise Template Style Brief before building the deck. It should be concrete enough for the user to judge whether the learned style is correct.

## Required Format

Use this structure:

```markdown
## Template Style Brief

### 1. Basic Information
- Reference type:
- Slide count / image count:
- Aspect ratio:
- Likely use case:
- Overall mood:

### 2. Visual System
- Primary colors:
- Accent colors:
- Background style:
- Typography:
- Icon/shape language:
- Header/footer/navigation:

### 3. Structure System
- Cover:
- Table of contents:
- Chapter divider:
- Body/content page:
- Figure/chart page:
- Regression/table page:
- Summary/closing:

### 4. Transfer Strategy
- Best-fit paper sections:
- Components to reuse:
- Components to adapt:
- Components to avoid:

### 5. Risks And Adjustments
- Readability risks:
- Missing fonts/assets:
- Long-deck risks:
- Recommended fixes:

### 6. Active Style Decision
- Strict clone / hybrid / light borrowing:
- Whether to keep default competition frame:
- Background image style:
```

## Decision Language

Use direct recommendations:

- `Recommended: hybrid transfer`
- `Recommended: strict style following`
- `Recommended: borrow only cover/chapter/color system`
- `Recommended: keep default competition frame and use template accents`

If the user does not answer, proceed with the recommended option and record it as an assumption.

## Mapping To Paper

After the brief, create a short mapping:

`paper section -> suggested reference page type -> expected slide count -> risk`

Example:

`Robustness -> question-led body page + table callout -> 6 slides -> table density risk`
