PAPER_TEX = paper.tex
PAPER_PDF = $(PAPER_TEX:.tex=.pdf)

SLIDES_TEX = slides.tex
SLIDES_PDF = $(SLIDES_TEX:.tex=.pdf)

PLOTS_ALL = plots/g.pdf plots/control.pdf plots/solution.pdf
PLOTS_PARAMETERS = plots/src/parameters.py
TABLES_ALL = tables/temperatures.tex
NUMERICALS_ALL = numericals/evo_temp.npy numericals/report.json

SOLVER = solver/core.py
ENV = env/problem.py env/parameters.py

.PHONY: paper slides \
		plots.all tables.all numericals.all \
		clean.plots clean.tables clean.numericals clean.all

# a dirty hack to make optenv package visible for the python scripts
# works only if make is called from the project root dir (which is normally the case)
export PYTHONPATH = :

paper: $(PAPER_PDF);

$(PAPER_PDF): \
		$(PAPER_TEX) \
		$(PLOTS_ALL) \
		$(TABLES_ALL)
	latexmk -pdf -g -silent $<

slides: $(SLIDES_PDF);

$(PLOTS_ALL): $(PLOTS_PARAMETERS) $(ENV)
$(NUMERICALS_ALL): $(SOLVER) $(ENV)

$(SLIDES_PDF): \
		$(SLIDES_TEX) \
		$(PLOTS_ALL) \
		$(TABLES_ALL)
	latexmk -xelatex -g -silent $<

plots/g.pdf: plots/src/g.py
	python3 plots/src/g.py --outfile=$@

plots/control.pdf: plots/src/control.py
	python3 plots/src/control.py --outfile=$@

plots/solution.pdf: \
		numericals/evo_temp.npy \
		plots/src/parameters.py \
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
clean.tables:
	rm -rf --interactive=never $(TABLES_ALL)
clean.numericals:
	rm -rf --interactive=never $(NUMERICALS_ALL)
