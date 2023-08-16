def candidaGORelationAnalyzer(file, go_search = None):
    """sumary_line
    A faster implementation of the gene ontology analyzer
    for the candida genomes, given the candida go ontology
    files and a search GO term, it extracts all the alt_id,
    relationship_ids and associated function with those
    gene ontology for the network analysis and to link with 
    the expression analysis.
    Keyword arguments:
    argument -- description
    file = goslim_candida.obo and go_search = gene ontology search terms
    Return: return_description
    a sorted list for direct import into the network analysis.
    """
    read_candida = list(filter(None,[x.strip() for x in open(file).readlines()]))
    candidaIterator = []
    for i in read_candida:
        if i.startswith("id:"):
            goslim = i.strip().replace("id:", "").replace(" ", "")
        if  i.startswith("is_a:") or \
                i.startswith("relationship:") \
                      or i.startswith("alt_id:"):
            gorelation = i.strip().replace("!", "|")       
            if i not in candidaIterator:
                candidaIterator.append([goslim, gorelation])
    return [j for i in ([candidaIterator[i] for i in range(len(candidaIterator)) \
                                  if candidaIterator[i][0] == go_search]) for j in i]
