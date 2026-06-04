# Evidence Image Handling

Use this reference before importing original paper figures, regression tables, screenshots, equation images, or PDF crops into a PPTX.

## Priority

- Original paper figures and tables are proof objects. They should usually be the largest visual element on evidence-led slides.
- Preserve aspect ratio. Never stretch a figure/table by forcing both width and height.
- Crop safe whitespace before scaling. The goal is to enlarge the evidence, not to decorate the slide.

## Crop Policy

Safe to remove:

- Large blank PDF margins.
- Page numbers, working-paper footers, download watermarks, and unrelated page furniture.
- Excess blank space above/below a table or chart.
- Long explanatory captions when the same meaning is rewritten as editable PPT text.

Do not remove:

- Table/figure titles when needed for identification.
- Panel labels such as Panel A/B.
- Axes, legends, units, row/column labels, significance stars, standard errors, notes needed to interpret coefficients.
- Formula symbols or assumptions that the slide discusses.

## Sizing Rules

- Evidence-led slides should allocate roughly 55-70% of usable content width to the original evidence image.
- If the original table is the only proof object, it may take nearly the full content area; use a short top/bottom callout for interpretation.
- If a dense table remains unreadable after safe crop and scaling, split it into:
  1. full-table context slide;
  2. key-row/key-column close-up slide.
- For multi-panel figures, either extract panels into a clean side-by-side layout or split panels across micro-slides.

## Import Modes

- `smart_crop`: default for PDF evidence. Crop safe white margins and page furniture, then contain-fit the crop.
- `wide_extract`: use when the figure/table body can be isolated from a full PDF page. Enlarge the extracted body.
- `contain`: fallback when cropping is uncertain. Preserve the whole image, but do not accept large internal whitespace if a safe crop is possible.
- `close_up`: use for regression tables, mechanism tables, and robustness batteries when key coefficients need to be readable.

## QA

- Render the deck to PNG and check the evidence at slide size, not only in the PPT editor.
- If the evidence cannot be read in the PNG preview, crop, enlarge, split, or create a close-up slide.
- Confirm the image remains proportional and no text-bearing content is squashed.
