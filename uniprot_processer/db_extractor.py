# module 5
import sys, os

def dbinsert_verification():
    for i in range(len(sys.argv)):
        if sys.argv[i] == "DBINSERT":
            if i == len(sys.argv)-1:
                print("Database not given")
                exit()
            elif not sys.argv[i+1].startswith("db="):
                print("Database not given right")
                exit()
            elif not os.path.isfile(sys.argv[i+1][3:]):
                print("The database given does not exist")
                exit()
            else:
                db_name = sys.argv[i+1][3:]
                return True


def table_dates(record):
    print("\n--TABLE DATES--")
    ID = ""
    DT = []
    for line in record:
        if line.startswith("ID"):
            ID = (line[5:].split(" ")[0])
    for line in record:
        if line.startswith("DT"):
            DT.append(line[5:])
    for i in range(0, len(DT)):
        print([ID , DT[i].split(",")[0], DT[i].split(",")[1]])

def table_names(record):
    print("\n--TABLE NAMES--")
    ID = ""
    DE = ""
    for line in record:
        if line.startswith("ID"):
            ID = (line[5:].split(" ")[0])
    for line in record:
        if line.startswith("DE"):
            DE = (line[5:])
            break
    print([ID , DE])
    
def table_codes(record):
    print("\n--TABLE CODES--")
    ID = ""
    DR = []
    for line in record:
        if line.startswith("ID"):
            ID = (line[5:].split(" ")[0])
    for line in record:
        if line.startswith("DR"):
            DR.append(line[5:])
    for i in range(0, len(DR)):
        print([ID , DR[i]])

def table_features(record):
    print("\n--TABLE FEATURES--")
    ID = ""
    for line in record:
        if line.startswith("ID"):
            ID = (line[5:].split(" ")[0])
            
    elemento = []
    contador = 0
    for line in record:
        if not line[5:].startswith(" ") and line.startswith("FT"):
            if not contador == 0:
                tipo = elemento[0].split()[0]
                loc = elemento[0].split()[1]
                info = ""
                for i in range(1, len(elemento)):
                    info += elemento[i][15:]
                print([ID, tipo, loc, info])
            elemento.clear()
            contador = 1
            elemento= [line[5:]]
        elif line[5:].startswith(" ") and line.startswith("FT"):
            elemento.append(line[5:])
    tipo = elemento[0].split()[0]
    loc = elemento[0].split()[1]
    info = ""
    for i in range(1, len(elemento)):
        info += elemento[i][15:]
    print([ID, tipo, loc, info])
       
def table_comments(record):
    print("\n--TABLE COMMENTS--")
    ID = ""
    for line in record:
        if line.startswith("ID"):
            ID = (line[5:].split(" ")[0])
            
    elemento = ""
    contador = 0
    for line in record:
        if line[5:].startswith("-!-") and line.startswith("CC"):
            if not contador == 0:
                print([ID, elemento])
            elemento = line[8:] 
            contador = 1           
        elif line[5:].startswith(" ") and line.startswith("CC"):
            elemento += line[8:]
        if line[5:].startswith("------") and line.startswith("CC"):
            print([ID, line[5:]])
        if line[5:].startswith("Copy") or line[5:].startswith("Dist"):
            print([ID, line[5:]])

from fasta_generator import get_header, get_sequence

def table_fasta(record):
    print("\n--TABLE FASTA--")
    ID = ""
    for line in record:
        if line.startswith("ID"):
            ID = (line[5:].split(" ")[0])
    header = get_header(record)
    sequence = get_sequence(record)
    print([ID, header, sequence])

def table_protein(record):
    print("\n--TABLE PROTEIN--")
    ID = ""
    for line in record:
        if line.startswith("ID"):
            ID = (line[5:].split(" ")[0])
    AC = ""
    for line in record:
        if line.startswith("AC"):
            AC += line[5:]
    OS = ""
    for line in record:
        if line.startswith("OS"):
            OS += line[5:]
    OC = ""
    for line in record:
        if line.startswith("OC"):
            OC += line[5:]
    OX = ""
    for line in record:
        if line.startswith("OX"):
            OX += line[5:]
    SQ = ""
    for line in record:
        if line.startswith("SQ"):
            SQ = line
            SQ += get_sequence(record)
    AA = ""
    for line in record:
        if line.startswith("ID"):
            AA += (line[5:].split()[2])
    KW = ""
    for line in record:
        if line.startswith("KW"):
            KW += line[5:]
    PE = ""
    for line in record:
        if line.startswith("PE"):
            PE += line[5:]
    GN = ""
    for line in record:
        if line.startswith("GN"):
            GN += line[5:]
    print([ID, AC, AA, GN, OS, OC, OX, KW, PE, SQ])

def db_printer(record):
    table_protein(record)
    table_dates(record)
    table_names(record)
    table_codes(record)
    table_features(record)
    table_comments(record)
    table_fasta(record)


def db_extractor(record):
    if dbinsert_verification():
        db_printer(record)
               
