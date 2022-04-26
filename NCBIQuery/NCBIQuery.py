# Main

import ssl
import sys
import pandas as pd
from Bio import Entrez
from extraction_module import extractor
ssl._create_default_https_context = ssl._create_unverified_context

# Obtener los IDs de todos los organismos que cumplan las condiciones
def search():
    query = sys.argv[1]
    Entrez.email = sys.argv[2]
    retmax_var = sys.argv[3]
    handleSearch = Entrez.esearch(db="Nucleotide", retmax=retmax_var, term=query)
    rec = Entrez.read(handleSearch)
    idlist = rec["IdList"]
    return idlist

# Obtener toda la info de cada ID, con extractor() filtro lo que me interesa y guardo todo en .tsv
def save():
    idlist = search()
    file = sys.argv[4]
    lista = []
    count=0
    for idorg in idlist:
        handleFetch = Entrez.efetch(db="nucleotide", retype="gb" ,id=idorg, retmode="xml")
        record = next(Entrez.parse(handleFetch))
        extractor(lista, record,idorg)
        count+=1
        print(count, " records inserted in table ", file)
    dfObj = pd.DataFrame(lista, columns=["ID", "Locus" ,"Length", "Strandedness", "Moltype", "Topology", "Division", "Primary-accession", "Organism", "Taxonomy"])
    dfObj.to_csv(file, sep='\t', index=False)
    print(file, "exported successfully")        


save()