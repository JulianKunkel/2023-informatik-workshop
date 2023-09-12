MAIN = git-exercise

PDF_CMD = pdflatex -shell-escape -interaction=nonstopmode $(MAIN).tex \
					&& pdflatex -shell-escape -interaction=nonstopmode $(MAIN).tex

all:
	$(PDF_CMD)

clean:
	rm -f $(MAIN).aux $(MAIN).bbl $(MAIN).bcf $(MAIN).blg $(MAIN).log $(MAIN).out $(MAIN).run.xml $(MAIN).toc $(MAIN).nav $(MAIN).snm $(MAIN).vrb $(MAIN).atfi
	rm -r _minted-$(MAIN)

