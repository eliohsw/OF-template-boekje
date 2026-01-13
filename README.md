# OF-template-boekje

A (lightweight), multipurpose, multilingual, multiplatform book template built for XeLaTeX.

To compile the document, type `make` or `make xelatexmk` in your terminal, or by clicking **Recompile** on Overleaf (make sure compiler `XeLaTeX` and main document `book.tex` are configured in the settings).

## Structure

- `book.tex` — The main LaTeX document
- `makefile` — Build automation script for compiling the document
- `latexmkrc` — Customize compile process
- `contents/` — Book contents (titlepage, preface, chapters, appendices, glossary, bibliography)
- `packages/` — Custom packages for specialized formatting and features
- `preamble/` — Document preamble configuration

## Initialization and Usage

Install [LaTeX](https://www.latex-project.org/get/) and [VS Code](https://code.visualstudio.com/download) if you intend to compile the document locally, ensure the [LaTeX Workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop) extension is working. Then, clone the repository from [GitHub](https://github.com/eliohsw/OF-template-boekje/) , or duplicate the project from [Overleaf](https://www.overleaf.com/read/rnkvhykqdxsk#c7c064) . 

1. In `book.tex` , set the `boekje` options for document language and features. Enable optional modules `boekje-label` for Chinese labels and `boekje-code` for code listings.
2. Configure fonts in `preamble/schrift.tex` (Latin and CJK lists). Install the fonts you select, or use fonts on your machine. For extra languages, uncomment `\input{preamble/sprache.tex}` and adjust its font declarations.
3. Customize headings and spacing in `preamble/stil.tex`. Add content in `contents/` and include new chapters or appendices via `\input{...}` in `book.tex` , and uncomment optional features in `book.tex` (glossary, index, bibliography) when needed.
4. Build locally with `make` or LaTeX Workshop.

> [!NOTE]
> For VS Code LaTeX Workshop integration, merge the LaTeX Workshop recipes/tools from `settings.jsonc` into your own settings. The template defaults to `make` for a clean, reproducible build.

> [!CAUTION]
> Custom minted styles are generated locally by `script/mint_injector.py` from `script/mint_styles.py` and cached in `_minted/*.style.minted` . Overleaf cannot generate these files due to restricted shell escape, so compile locally and commit the cached style file if you need to use Overleaf. This cache workaround is not ideal, but it is the current approach.

## Recommendations

This template supports multilingual documents via Polyglossia, primarily handling Latin (English, German) and CJK text. If other languages are needed, adjust the corresponding Polyglossia settings.

Additional font and language settings can be adjusted in `preamble/schrift.tex` and `preamble/sprache.tex` .  However, it is recommended to install the following fonts on your machine for better aesthetics:

1. [Fandol fonts](https://ctan.org/tex-archive/fonts/fandol) for (simplified) Chinese typesetting
3. [Source Han Sans](https://github.com/adobe-fonts/source-han-sans/releases) fonts
4. [Source Han Serif](https://github.com/adobe-fonts/source-han-serif/releases) fonts
5. [CMU](https://ctan.org/tex-archive/fonts/cm-unicode) fonts (the Computer Modern Unicode font family)
6. [Source Sans 3](https://fonts.google.com/specimen/Source+Sans+3) or [Noto Sans](https://fonts.google.com/noto/specimen/Noto+Sans)
7. [Source Code Pro](https://github.com/adobe-fonts/source-code-pro) or [JetBrains Mono](https://github.com/JetBrains/JetBrainsMono)

It is recommended to compile the document on your own machine, since the font support on Overleaf is limited.

> [!NOTE]
> Currently, XeLaTeX does not support variable fonts. Make sure the correct font files are installed.
