# ontoloty-network-candida

i coded this a faster implementation of the gene ontology analyzer for the candida genomes, given the candida go ontology files and a search GO term, it extracts all the alt_id,  relationship_ids and associated function with those  gene ontology for the network analysis and to link with  the expression analysis. This is a test ontology term, you can use any ontology term that you are interested in for making your expression networks. The reason, why i coded this, is that if i look at the candida genome database, i was not able to find the associated gene ontologies associated with a specific ontology that i can plot along with the expression into a directed acyclic graph, so i coded this and given an ontology term and the gene ontology file, it will give you all the associated IDs as well as the function. The ids can be directly used as a iterable in the network analysis to plot along with the expression as edges and nodes. 

```
candidaGORelationAnalyzer("/Users/gauravsablok/Desktop/CodeCheck/broad/goslim_candida.obo",
                         go_search="GO:0042493")
['GO:0042493',
 'alt_id: GO:0017035',
 'GO:0042493',
 'is_a: GO:0042221 | response to chemical']
```
Gaurav \
Academic Staff Member \
Bioinformatics \
Institute for Biochemistry and Biology \
University of Potsdam \
Potsdam,Germany 
