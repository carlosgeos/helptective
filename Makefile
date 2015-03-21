TEXFILE = main

$(TEXFILE).pdf: $(TEXFILE).tex
	latexmk -xelatex -output-directory=tex_files $(TEXFILE)

view: $(TEXFILE).pdf
	evince tex_files/$(TEXFILE).pdf &

clean:
	rm -frv tex_files
