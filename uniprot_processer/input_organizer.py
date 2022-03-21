# module 2
import sys
import os

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
        elif x == "DBINSERT":
            inputs_list.append("DBINSERT")
    return inputs_list
