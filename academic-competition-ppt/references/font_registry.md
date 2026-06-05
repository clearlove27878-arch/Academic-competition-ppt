# Font Registry

Use this registry when selecting, embedding, copying, or packaging fonts for long-form Chinese academic paper PPT decks.

## Compliance Rule

Do not bundle, redistribute, or embed commercial, system, member-only, or license-unclear fonts by default. A font may be placed in `assets/fonts/` only when its license permits the intended use. If license status is uncertain, reference the font by family name and provide fallbacks instead of packaging the file.

## Registered Fonts

| Font | Role | Packaging Status | Use |
|---|---|---|---|
| 思源宋体 CN Heavy | Default Chinese title serif | Package only if a licensed copy is available | Cover title, chapter title, page title, formal nav, academic emphasis |
| Source Han Serif CN Heavy / Noto Serif CJK SC Heavy | Fallback title serif | Usually installed or package if licensed | Same role as 思源宋体 CN Heavy |
| 053-上首逸飞体 | Decorative hard-tech accent | Do not package unless license explicitly permits | Tech/hardcore style accent only |
| 演示流动云楷 | Decorative ink/calligraphic accent | Do not package unless license explicitly permits | Ink/humanities/ecological accent only |
| Source Han Sans SC / Noto Sans CJK SC | Preferred Chinese sans body | Package only if licensed; otherwise use installed font | Body, tables, labels, footnotes |
| Microsoft YaHei / 微软雅黑 | System fallback only | Do not package in skill | Body fallback on Windows |
| Times New Roman | English academic serif | System/application fallback; do not package | English title, paper info, references, English quotes |
| Cambria Math | Formula fallback | System/application fallback; do not package | Editable math if original formula font is unstable |

## Font Family Fallback Stacks

- Chinese title stack: `思源宋体 CN Heavy` -> `Source Han Serif CN Heavy` -> `Noto Serif CJK SC Heavy` -> `SimSun` -> `Microsoft YaHei`.
- Chinese body stack: `Source Han Sans SC` -> `Noto Sans CJK SC` -> `Microsoft YaHei` -> `SimHei`.
- Chinese table/label stack: `Source Han Sans SC` -> `Noto Sans CJK SC` -> `Microsoft YaHei` -> `Arial`.
- English academic stack: `Times New Roman` -> `Georgia` -> `Cambria`.
- Formula stack: preserve original formula font -> `Cambria Math` -> `Times New Roman`; use high-resolution formula screenshot if replacement changes symbols or layout.
- Tech accent stack: `053-上首逸飞体` -> `思源宋体 CN Heavy` -> Chinese title stack.
- Ink accent stack: `演示流动云楷` -> `思源宋体 CN Heavy` -> Chinese title stack.

## Asset Directory

`assets/fonts/` is reserved for fonts with clear redistribution/embedding permission. Keep a short source/license note near any packaged font when possible. Do not place Microsoft YaHei, Times New Roman, Cambria Math, or other system/application fonts in this directory.

## Missing Font Behavior

If a selected font is missing:

1. Use the corresponding fallback stack.
2. Preserve Chinese glyph coverage and text fit.
3. Re-check title wrapping, navigation width, table legibility, and formula accuracy.
4. Do not stop deck generation merely because a decorative font is unavailable.
