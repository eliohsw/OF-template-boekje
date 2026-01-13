.PHONY: all xelatexmk clean

LATEXMK_FLAGS = -xelatex -synctex=1 -file-line-error -interaction=nonstopmode -halt-on-error -shell-escape

ifeq ($(OS),Windows_NT)
  RM_AUX = powershell -NoProfile -Command "Remove-Item -Force -ErrorAction SilentlyContinue *.acn,*.acr,*.alg,*.aux,*.auxlock,*.bbl,*.bcf,*.blg,*.fdb_latexmk,*.figlist,*.fls,*.glg,*.glo,*.gls,*.idx,*.ilg,*.ind,*.ist,*.listing,*.lof,*.log,*.lot,*.makefile,*.nav,*.out,*.run.xml,*.snm,*.synctex.gz,*.toc,*.vrb,*.xdv,*-SAVE-ERROR"
  RM_MINTED = powershell -NoProfile -Command "if (Test-Path _minted) { Get-ChildItem -Path _minted -File -Recurse | Where-Object { $_.Name -notlike '*.style.minted' } | Remove-Item -Force }"
  RM_PYCACHE = powershell -NoProfile -Command "Get-ChildItem -Path . -Directory -Recurse -Force -Filter '__pycache__' | Remove-Item -Recurse -Force"
else
  RM_AUX = rm -f *.acn *.acr *.alg *.aux *.auxlock *.bbl *.bcf *.blg *.fdb_latexmk \
		*.figlist *.fls *.glg *.glo *.gls *.idx *.ilg *.ind *.ist *.listing \
		*.lof *.log *.lot *.makefile *.nav *.out *.run.xml *.snm *.synctex.gz \
		*.toc *.vrb *.xdv *-SAVE-ERROR
  RM_MINTED = if [ -d _minted ]; then find _minted -type f \( -name '*.style.minted' -prune \) -o -type f -delete; fi
  RM_PYCACHE = find . -type d -name '__pycache__' -prune -exec rm -rf {} +
endif

all: xelatexmk

xelatexmk:
	latexmk $(LATEXMK_FLAGS) book.tex

clean:
	@$(RM_AUX)
	@$(RM_MINTED)
	@$(RM_PYCACHE)
