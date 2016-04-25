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
#sparqlEndpointGo = "http://localhost:3030/go/query" # fuseki
sparqlEndpointGo = "http://localhost:8890/sparql" # virtuoso
filePathQueryHierarchy = "getDescendantsHierarchy.sparql"
filePathResultLabel = "go-BP-hierarchy.lp"
verboseComment = True # each ASP line ends with a human-readable comment using the labels of the GO terms instead of their identifiers
if verboseComment:
    filePathResultLabel = filePathResultLabel[:-3] + "-withComments.lp"


t0 = time.time()


sparql = SPARQLWrapper(sparqlEndpointGo)
query = open(filePathQueryHierarchy).read()
sparql.setQuery(query)
sparql.setReturnFormat(JSON)
results = sparql.query().convert()
nbResults = 0

with open(filePathResultLabel, "w") as resultFile:
    for result in results["results"]["bindings"]:
        nbResults += 1
        resultFile.write(result["relationLabel"]["value"] + "(" + result["descendant"]["value"].replace("http://purl.obolibrary.org/obo/GO_", "go_") + ", " + result["superCl"]["value"].replace("http://purl.obolibrary.org/obo/GO_", "go_") + "). ")
        if verboseComment:
            resultFile.write("% " + result["relationLabel"]["value"] + "(\"" + result["descendantLabel"]["value"] + "\", \"" + result["superLabel"]["value"] + "\")" )
        resultFile.write("\n")
print("")
print("Nb results: " + str(nbResults))

t1 = time.time()
print("")
print("Query duration: " + str(t1 - t0))
