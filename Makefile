
.PHONY: Data
Data:
	bash src/download_data.sh

.PHONY: config
config:
	mkdir data results

.PHONY: clean
clean:
	rm -r data results
