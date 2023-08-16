# candida_ontology_network_analyzer
A faster implementation of the gene ontology analyzer for the candida genomes, given the candida go ontology files and a search GO term, it extracts all the alt_id,  relationship_ids and associated function with those  gene ontology for the network analysis and to link with  the expression analysis. This is a test ontology term, you can use any ontology term that you are interested in for making your expression networks. 

```
candidaGORelationAnalyzer("/Users/gauravsablok/Desktop/CodeCheck/broad/goslim_candida.obo", go_search="GO:0042493")
['GO:0042493',
 'alt_id: GO:0017035',
 'GO:0042493',
 'is_a: GO:0042221 | response to chemical']
```
