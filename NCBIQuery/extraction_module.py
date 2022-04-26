# Module 1

# Extraer los datos que me interesan y añadirlos al dictionary
def extractor(lista, record, idorg):
    lista.append([idorg, record['GBSeq_locus'], 
                         record['GBSeq_length'], 
                         record['GBSeq_strandedness'], 
                         record['GBSeq_moltype'],
                         record['GBSeq_topology'], 
                         record['GBSeq_division'],
                         record['GBSeq_primary-accession'], 
                         record['GBSeq_organism'],
                         record['GBSeq_taxonomy']])
