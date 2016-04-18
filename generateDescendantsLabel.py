#! /usr/bin/env python

# retrieve the latest GO ontology from http://purl.obolibrary.org/obo/go.owl

from SPARQLWrapper import SPARQLWrapper, JSON
import time

# BP = go:0008150
# CC = go:0005575
# MF = go:0003674

##########
###
### PARAMETERS
###
##########
sparqlEndpointGo = "http://localhost:3030/go/query" # fuseki
#sparqlEndpointGo = "http://localhost:8890/sparql" # virtuoso
filePathQueryLabel = "getDescendantsLabel.sparql"
filePathResultLabel = "go-BP-labels.lp"

t0 = time.time()


sparql = SPARQLWrapper(sparqlEndpointGo)
query = open(filePathQueryLabel).read()
sparql.setQuery(query)
sparql.setReturnFormat(JSON)
results = sparql.query().convert()
nbResults = 0
# for result in results["results"]["bindings"]:
#     nbResults += 1
#     print("")
#     print(result["descendant"]["value"] + "  ===>  " + result["descendantLabel"]["value"])
# print("")
# print("Nb results: " + str(nbResults))

with open(filePathResultLabel, "w") as resultFile:
    for result in results["results"]["bindings"]:
        nbResults += 1
        resultFile.write("label(" + result["descendant"]["value"].replace("http://purl.obolibrary.org/obo/GO_", "go_") + ", \"" + result["descendantLabel"]["value"] + "\").\n")
print("")
print("Nb results: " + str(nbResults))

t1 = time.time()
print("")
print("Query duration: " + str(t1 - t0))
