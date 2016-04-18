# go2asp

go2asp is a collection of SPARQL queries and scripts for generating as ASP representation of the [Gene Ontology](http://geneontology.org/).

----------
## Getting started

### Requirements

* a SPARQL endpoint for accessing the Gene Ontology
* [sparqlwrapper](https://rdflib.github.io/sparqlwrapper/) for the Python scripts

### Usage

Currently, the scripts have to be run manually:
* `generateDescendantsLabel.py` generates a list of predicates `label(go_0000001, "mitochondrion inheritance")` in the `file go-BP-labels.lp`
* `generateDescendantsHierarchy.py`generates a list of predicates `subClassOf(go_0000003, go_0008150).` in the file `go-BP-hierarchy.lp` (if the parameter `verboseComment` is FALSE) or in the file `go-BP-hierarchy-withComments.lp` (if the parameter `verboseComment` is TRUE).


## TODO
* add a makefile or a Snakefile
* add instructions for setting up a local SPARQL endpoint of the Gene Ontology

