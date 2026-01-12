.PHONY: all xelatexmk clean

all: xelatexmk

xelatexmk:
	TEXINPUTS=./packages//: latexmk -xelatex -synctex=1 -file-line-error -interaction=nonstopmode -halt-on-error book.tex

clean:
	rm -f *.aux *.auxlock *.bbl *.bcf *.blg *.fdb_latexmk *.figlist *.fls \
			*.idx *.ilg *.ind *.lof *.log *.lot *.makefile *.nav *.out \
			*.run.xml *.snm *.synctex.gz *.toc *.vrb *.xdv *-SAVE-ERROR