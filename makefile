.PHONY: all xelatexmk clean

all: xelatexmk

xelatexmk:
	TEXINPUTS=./packages//: latexmk -xelatex -synctex=1 -file-line-error -interaction=nonstopmode -halt-on-error -shell-escape book.tex

clean:
	rm -f *.aux *.auxlock *.bbl *.bcf *.blg *.fdb_latexmk *.figlist *.fls \
			*.idx *.ilg *.ind *.listing *.lof *.log *.lot *.makefile *.minted *.nav *.out \
			*.run.xml *.snm *.synctex.gz *.toc *.vrb *.xdv *-SAVE-ERROR \
			_minted/*
