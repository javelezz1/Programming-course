
# Made by Jhon Alexander Velez Zapata


import os
import sys

def inputs():
    if len(sys.argv) == 1:
        print("Filename not provided")
        exit()
    elif len(sys.argv) == 2:
        print("Query not given")
        exit()
    elif len(sys.argv) > 2:
        query = sys.argv[2].split(".and.")
        fields = sys.argv[3:]
        filename = sys.argv[1]
        if not os.path.isfile(filename):
            print("The file given does not exist")
            exit()
    return query, fields, filename

def comandos()->list:
    inputs_list = []
    for x in sys.argv:
        if x == "COUNTALL":
            inputs_list.append("COUNTALL")
        elif x == "COUNT":
            inputs_list.append("COUNT")
        elif x == "SHOWALL":
            inputs_list.append("SHOWALL")
        elif x == "TAXONS":
            inputs_list.append("TAXONS")
        elif x == "FASTA":
            inputs_list.append("FASTA")
    return inputs_list

def verificar_registro(record:list, query:list)->bool:
    
    conditions = len(query)
    for logic in query:
        value,fieldkey = logic.split(".in.")
        for field in record:
            fieldname = field[:2]
            fieldvalue = field[2:].strip()
            if not fieldkey=="SQ":
                if fieldname == fieldkey and value in fieldvalue:
                    conditions -= 1
                    break
            elif value in fieldvalue:
                conditions-=1
                break
    return conditions == 0

def procesar_proteinas():
    inputs_list=comandos()
    query, fields, filename = inputs()
    handle = open(filename, mode="rt")
    count:int = 0
    countall:int = 0
    record=[]
    lista_taxones = []
    for line in handle:
        if line.startswith("ID"):
            record.clear()
            record= [line[:-1]]
        elif line.startswith("//"):
            if verificar_registro(record,query):
                count += 1
                if "FASTA" in inputs_list:
                    fasta(record)
                elif "TAXONS" in inputs_list:
                    taxons = taxon_id(record)
                    for taxon in taxons:
                        lista_taxones.append(taxon)
                if len(sys.argv) < 4 or "SHOWALL" in inputs_list:
                    for f in record:
                        print(f)
                else:
                    if not "FASTA" in inputs_list:
                        field_printer(record, inputs_list)
            countall += 1
        else:
            record.append(line[:-1])
    if "TAXONS" in inputs_list:
        taxon_count(lista_taxones)
    handle.close()
    if not "FASTA" in inputs_list:
        llamada_comandos(count, countall, inputs_list)

def field_printer(record,inputs_list):
    for field in sys.argv[3+len(inputs_list):]:
        for line in record:
            if line.startswith(field):
                print(line)
            elif "SQ" in sys.argv and line.startswith("  "):
                print(line)

def llamada_comandos(count, countall, inputs_list):
    if "COUNT" in inputs_list:
        print(count)
    if "COUNTALL" in inputs_list:
        print(countall)
    if "COUNT" in inputs_list and "COUNTALL" in inputs_list:
        print("{0:6.3f}%".format(count*100/countall))

def get_header(record:list)->str:
    fasta_header = ""
    for field in record:
        if field.startswith("ID"):
            fasta_header += "id=" + field.split()[1]+";"
        elif field.startswith("AC"):
            accs = "" 
            for acc in field.split()[1:]:
                accs += acc
            fasta_header += "accesion=" + accs
        elif field.startswith("OS"):
            names = ""
            for name in field[5:]:
                names += name
            fasta_header += "name=" + names
    return fasta_header

def get_sequence(record:list)->str:
    fasta_sequence = ""
    for field in record:
        if field.startswith("  "):
            fasta_sequence += field
    sequence_2 = ""
    sequence = fasta_sequence.replace(" ", "").replace("\n", "")
    for i in range(0, len(sequence), 90):
        sequence_2 += sequence[i: i+90] + "\n"
    return sequence_2

def fasta(record:list):
    fastastring = ">" + get_header(record)
    fastastring += "\n" + get_sequence(record)
    print(fastastring)

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


procesar_proteinas()