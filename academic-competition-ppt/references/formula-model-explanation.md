# Formula And Model Explanation

Use this for every formula, econometric model, theoretical model, index construction, or identification page.

## Required Questions

Every formula/model page must answer:

- What question does this model answer?
- What are the dependent variable, core explanatory variable, mediators/moderators, and controls?
- What does the key coefficient mean?
- What do fixed effects, controls, clustering, instruments, matching, thresholds, or event-time terms try to exclude?
- What assumption is needed?
- What can this model not answer?

## Explanation Pattern

For complex methods, use:

`wrong/simple method -> why it is wrong -> paper method -> economic intuition -> coefficient interpretation -> boundary`.

Examples:

- OLS may mix treatment effect with unobserved firm traits; fixed effects compare within-unit changes after removing stable differences.
- DID is not just a regression label; it asks whether treated and control groups would have moved similarly without the shock.
- Mediation is not proof of the whole causal mechanism unless the design supports the path interpretation.

## Layout Pattern

- Put the formula in a large readable panel or high-resolution crop; it should be the visual anchor, not a tiny box.
- Put symbol decoding in a tidy grid or side panel.
- Add a right-side or adjacent block: `回答什么问题`.
- Add one source-driven explanatory paragraph, not only short labels.
- Add a bottom boundary/takeaway: what the model excludes, assumes, or cannot prove.
- Put economic meaning in editable text.
- Use arrows or highlights to focus on the key coefficient.
- If editable math breaks Chinese, superscripts, or symbols, use a clean screenshot for the equation and editable text for explanation.
