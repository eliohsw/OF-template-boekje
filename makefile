.PHONY: all xelatexmk clean

all: xelatexmk

xelatexmk:
	latexmk -xelatex -synctex=1 -file-line-error -interaction=nonstopmode -halt-on-error -shell-escape book.tex

clean:
	@rm -f *.acn *.acr *.alg *.aux *.auxlock *.bbl *.bcf *.blg *.fdb_latexmk \
			*.figlist *.fls *.glg *.glo *.gls *.idx *.ilg *.ind *.ist *.listing \
			*.lof *.log *.lot *.makefile *.nav *.out *.run.xml *.snm *.synctex.gz \
			*.toc *.vrb *.xdv *-SAVE-ERROR
	@if [ -d _minted ]; then \
		find _minted -type f \( -name '*.style.minted' -prune \) -o -type f -delete; \
	fi
	@find . -type d -name '__pycache__' -prune -exec rm -rf {} +
