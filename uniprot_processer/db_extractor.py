# module 5
import sys, os
from sqlite3_connections import insertion
from input_organizer import comandos

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
                print("The given database does not exist")
                exit()
            else:
                db_name = sys.argv[i+1][3:]
                return True, db_name

def table_dates(record):
    ID = ""
    DT = []
    for line in record:
        if line.startswith("ID"):
            ID = (line[5:].split(" ")[0])
    for line in record:
        if line.startswith("DT"):
            DT.append(line[5:])
    TABLEDATES = []
    for i in range(0, len(DT)):
        TABLEDATES.append([ID , DT[i].split(",")[0], DT[i].split(",")[1]])
    return TABLEDATES

def table_names(record):
    ID = ""
    DE = ""
    for line in record:
        if line.startswith("ID"):
            ID = (line[5:].split(" ")[0])   
    elemento = ""
    contador = 0
    TABLENAMES = []
    for line in record:
        if not line[5:].startswith("  ") and line.startswith("DE"):
            if not contador == 0:
                TABLENAMES.append([ID, elemento])
            elemento = line[5:] 
            contador = 1           
        elif line[5:].startswith(" ") and line.startswith("DE"):
            elemento += line[8:]
    TABLENAMES.append([ID, elemento])
    return TABLENAMES
 
def table_codes(record):
    ID = ""
    DR = []
    for line in record:
        if line.startswith("ID"):
            ID = (line[5:].split(" ")[0])
    for line in record:
        if line.startswith("DR"):
            DR.append(line[5:])
    TABLECODES = []
    for i in range(0, len(DR)):
        TABLECODES.append([ID , DR[i]])
    return TABLECODES

def table_features(record):
    ID = ""
    for line in record:
        if line.startswith("ID"):
            ID = (line[5:].split(" ")[0])
    TABLEFEATURES = []        
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
                TABLEFEATURES.append([ID, tipo, loc, info])
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
    TABLEFEATURES.append([ID, tipo, loc, info])
    return TABLEFEATURES
       
def table_comments(record):
    ID = ""
    for line in record:
        if line.startswith("ID"):
            ID = (line[5:].split(" ")[0])
    TABLECOMMENTS = []
    elemento = ""
    contador = 0
    linea_final_contador = 0
    for line in record:
        if line[5:].startswith("-!-") and line.startswith("CC"):
            if not contador == 0:
                TABLECOMMENTS.append([ID, elemento])
            elemento = line[8:] 
            contador = 1           
        elif line[5:].startswith(" ") and line.startswith("CC"):
            elemento += line[8:]
        if line[5:].startswith("------") and line.startswith("CC"):
            if linea_final_contador == 0:
                TABLECOMMENTS.append([ID, elemento])
                linea_final_contador = 1
            TABLECOMMENTS.append([ID, line[5:]])
        if line[5:].startswith("Copy") or line[5:].startswith("Dist"):
            TABLECOMMENTS.append([ID, line[5:]])
    return TABLECOMMENTS

from fasta_generator import get_header, get_sequence

def table_fasta(record):
    ID = ""
    for line in record:
        if line.startswith("ID"):
            ID = (line[5:].split(" ")[0])
    header = get_header(record)
    sequence = get_sequence(record)
    TABLEFASTA = [ID, header, sequence]
    return TABLEFASTA

def table_protein(record):
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
    TABLEPROTEIN = []
    TABLEPROTEIN.append([ID, AC, AA, GN, OS, OC, OX, KW, PE, SQ])
    return TABLEPROTEIN

def db_printer(TABLECOMMENTS, TABLEDATES, TABLEFEATURES, TABLENAMES, TABLEFASTA, TABLECODES, TABLEPROTEIN):
    print("\n--TABLE PROTEIN--")
    print(TABLEPROTEIN)
    print("\n--TABLE DATES--")
    for i in TABLEDATES:
        print(i)
    print("\n--TABLE NAMES--")
    for i in TABLENAMES:
        print(i)
    print("\n--TABLE CODES--")
    for i in TABLECODES:
        print(i)
    print("\n--TABLE FEATURES--")
    for i in TABLEFEATURES:
        print(i)
    print("\n--TABLE COMMENTS--")
    for i in TABLECOMMENTS:
        print(i)
    print("\n--TABLE FASTA--")
    print(TABLEFASTA)
       
def sqlite3_options(record):
    id_protein=""
    for line in record:
        if line.startswith("ID"):
            id_protein = (line[5:].split(" ")[0])
    boolean, db_name = dbinsert_verification()
    if boolean == True:
        TABLEPROTEIN=table_protein(record)
        TABLEDATES=table_dates(record)
        TABLENAMES=table_names(record)
        TABLECODES=table_codes(record)
        TABLEFEATURES=table_features(record)
        TABLECOMMENTS=table_comments(record)
        TABLEFASTA=table_fasta(record)
        inputs_list=comandos()
        insertion(TABLECOMMENTS, TABLEDATES, TABLEFEATURES, TABLENAMES, TABLEFASTA, TABLECODES, TABLEPROTEIN, db_name, id_protein)
        if "VERBOSE" in inputs_list:
            db_printer(TABLECOMMENTS, TABLEDATES, TABLEFEATURES, TABLENAMES, TABLEFASTA, TABLECODES, TABLEPROTEIN)
         
