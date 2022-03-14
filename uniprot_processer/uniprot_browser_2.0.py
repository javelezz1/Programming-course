
# Made by Jhon Alexander Velez Zapata

from fasta_generator import fasta
from input_organizer import comandos, inputs
from basic_commands import verificar_registro, field_printer, llamada_comandos
from taxon_command import taxon_count, taxon_id
import sys


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


procesar_proteinas()