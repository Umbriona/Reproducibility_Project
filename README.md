# Reproducibility project
In this project we try to answer whether proteins with a large number of interactions also have a larger amount of registered pfam domains.

## Requirements

This project was validated on Ubuntu 18.04 and singularity version 3.7.0

## Running code

To reproduce the results run  `make` 
To run tests run `python -m unittest`

If you want to set other thresholds for connections or classifying value you can change that in the Makefile with the variables CONNECTION and CLASS.  

## Singularity 

If you want to remake the singularity image you can use the recipe image.def either as is or modify it for your needs. To build run 
` sudo singularity build image.sif image.def `

The conda dependencies can be managed in environment.yml

## Results
As seen in the plot the median proteins that have more than 100 interactions more registered interactions also have more registered pfam domains on average.
The proteins that had no registered pfam domains were excluded from the statistics.
New results are saved in the results directory.

![alt text](boxplot.png "Boxplot")
