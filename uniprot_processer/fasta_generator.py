# module 1

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
