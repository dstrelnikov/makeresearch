PAPER_TEX = paper.tex
PAPER_PDF = $(PAPER_TEX:.tex=.pdf)

SLIDES_TEX = slides.tex
SLIDES_PDF = $(SLIDES_TEX:.tex=.pdf)

PLOTS_ALL = plots/g.pdf plots/control.pdf plots/solution.pdf
TABLES_ALL = tables/temperatures.tex
NUMERICALS_ALL = numericals/evo_temp.npy numericals/report.json

SOLVER = solver/core.py
ENV = env/problem.py
%: $(SOLVER) $(ENV);

.PHONY: paper slides \
		plots.all tables.all numericals.all \
		clean.plots clean.tables clean.numericals clean.all


paper: $(PAPER_PDF);

$(PAPER_PDF): \
		$(PAPER_TEX) \
		$(PLOTS_ALL) \
		$(TABLES_ALL)
	latexmk -pdf -silent $<

slides: $(SLIDES_PDF);

$(SLIDES_PDF): \
		$(SLIDES_TEX) \
		$(PLOTS_ALL) \
		$(TABLES_ALL)
	latexmk -pdf -silent $<

plots/g.pdf: plots/src/g.py
	python3 plots/src/g.py --outfile=$@

plots/control.pdf: plots/src/control.py
	python3 plots/src/control.py --outfile=$@

plots/solution.pdf: \
		numericals/evo_temp.npy \
		plots/src/solution.py
	python3 plots/src/solution.py --evo=$< --outfile=$@

tables/temperatures.tex: \
		numericals/report.json \
		tables/src/temperatures.py
	python3 tables/src/temperatures.py --report=$< > $@

numericals/evo_temp.npy: numericals/src/compute.py
	python3 numericals/src/compute.py --outfile=$@

numericals/report.json: \
		numericals/evo_temp.npy \
		numericals/src/report.py
	python3 numericals/src/report.py --evo=$< --outfile=$@


plots.all: $(PLOTS_ALL);
tables.all: $(TABLES_ALL)
numericals.all: $(NUMERICALS_ALL)


clean.all: clean.plots clean.tables clean.numericals
	latexmk -C
clean.plots:
	rm -rf --interactive=never $(PLOTS_ALL)
clean.talbes:
	rm -rf --interactive=never $(TABLES_ALL)
clean.numericals:
	rm -rf --interactive=never $(NUMERICALS_ALL)
