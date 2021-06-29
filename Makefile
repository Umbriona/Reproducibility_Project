DATA_DIR=data/

#Files
PROTEIN_DOMAINS = protein_domains.txt
PROTEIN_INTERACTIONS = protein_links.txt

.PHONY: Data
Data:
	bash src/download_data.sh

boxplot.png: Data
	python -m src.main -d $(DATA_DIR)$(PROTEIN_INTERACTIONS) -p $(DATA_DIR)$(PROTEIN_DOMAINS)

.PHONY: clean
clean:
	rm -r data results
