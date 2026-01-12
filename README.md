# OF-template-boekje

A lightweight, multipurpose, multiplatform book template built for XeLaTeX.

This template supports multilingual documents via Polyglossia, primarily handling Latin and CJK text.

To compile the document, type `make` or `make xelatexmk` in your terminal, or by clicking **Recompile** on Overleaf (make sure compiler `XeLaTeX` and main document `book.tex` are configured in the settings).

## Structure

- **book.tex** — The main LaTeX document
- **makefile** — Build automation script for compiling the document
- **contents/** — Book contents (titlepage, preface, chapters, appendices, glossary, bibliography)
- **packages/** — Custom packages for specialized formatting and features
- **preamble/** — Document preamble configuration

## Usage

Review the load options for **set-memoir.sty**, configure font settings in **schrift.tex**, enable multilingual settings by uncommenting **sprache.tex**, and edit the style of the book in **stil.tex**. Edit each file for your preferences.

## Recommendations

Additional font and language settings can be adjusted in **preamble/schrift.tex** and **preamble/sprache.tex**.  However, it is recommended to install the following fonts on your machine for better aesthetics:

1. [Fandol fonts](https://ctan.org/tex-archive/fonts/fandol) for (simplified) Chinese typesetting
3. [Source Han Sans](https://github.com/adobe-fonts/source-han-sans/releases) fonts
4. [Source Han Serif](https://github.com/adobe-fonts/source-han-serif/releases) fonts
5. [CMU](https://ctan.org/tex-archive/fonts/cm-unicode) fonts (the Computer Modern Unicode font family)
6. [Source Sans 3](https://fonts.google.com/specimen/Source+Sans+3) or [Noto Sans](https://fonts.google.com/noto/specimen/Noto+Sans)

It is recommended to compile the document on your own machine, since the font support on Overleaf is limited.

> [!NOTE]
> Currently, XeLaTeX does not support variable fonts. Make sure the correct font files are installed.
