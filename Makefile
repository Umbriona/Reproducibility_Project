DATA_DIR=/data/
RESULT_DIR=/results/

#Files
PROTEIN_DOMAINS = protein_domains.txt
PROTEIN_INTERACTIONS = protein_links.txt

# Var
CONNECTIONS = 500
CLASS = 100

all: boxplot.png

# setup data files and results directory
.PHONY: Data
Data:
	mkdir -p results
	bash src/download_data.sh

boxplot.png: Data
	singularity exec --bind data:/data,src:/src,results:/results image.sif python /src/main.py -d $(DATA_DIR)$(PROTEIN_INTERACTIONS) -p $(DATA_DIR)$(PROTEIN_DOMAINS) -o $(RESULT_DIR)protein_domains_vs_string_degree.png -c $(CONNECTIONS) -n $(CLASS)

.PHONY: clean
clean:
	rm -r data results
	rm *.sif
