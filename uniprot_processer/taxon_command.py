# module 4

def taxon_id(record):
    taxon_list= []
    taxons = []
    for l in record:
        if l.startswith("OC"):
            taxon_list.append(l.split()[1:])
    for part in taxon_list:
        for taxon in part:
            taxons.append(taxon)
    return taxons

def taxon_count(lista_taxones):
    counts = []
    usados = []
    clados = []
    taxon_dictionary = []            
    for taxon in lista_taxones:
        taxon=taxon.replace(";", "")
        taxon=taxon.replace(".", "")
        clados.append(taxon)
    for clado in clados:
        if clado not in usados:
            counts.append(str(clados.count(clado)))
            usados.append(clado)
    for i in range(0, len(counts)):
        taxon_dictionary.append((usados[i], counts[i]))
    for c in taxon_dictionary:
        print(c[0] + " " + c[1])
