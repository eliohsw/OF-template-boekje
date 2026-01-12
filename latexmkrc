# Use xelatex as the engine
$pdflatex = 'xelatex -synctex=1 -file-line-error -interaction=nonstopmode -halt-on-error -shell-escape %O %S';

# Set the main document
$root = 'book.tex';