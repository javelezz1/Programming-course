# module 6

import sqlite3


def delete(conn, id_protein):
    sql ="PRAGMA foreign_keys = ON;"
    conn.execute(sql)
    sql = "DELETE FROM Proteins WHERE idprotein == '{}'".format(id_protein)
    conn.execute(sql)
    

def sqlite_generator(conn, TABLECOMMENTS, TABLEDATES, TABLEFEATURES, TABLENAMES, TABLEFASTA, TABLECODES, TABLEPROTEIN):
    for i in TABLEPROTEIN:
        conn.execute("INSERT INTO Proteins(idprotein, accession, AA_number, orfnames, names, taxonomy, taxonomyid, keywords, predicted, sequence) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]))
    for i in TABLECOMMENTS:
        conn.execute("INSERT INTO Comments VALUES(?, ?)", (i[0], i[1]))
    for i in TABLEDATES:
        conn.execute("INSERT INTO Dates VALUES(?, ?, ?)", (i[0], i[1], i[2]))
    for i in TABLEFEATURES:
        conn.execute("INSERT INTO Features VALUES(?, ?, ?, ?)", (i[0], i[1], i[2], i[3]))
    for i in TABLENAMES:
        conn.execute("INSERT INTO Names VALUES(?, ?)", (i[0], i[1]))
    for i in [TABLEFASTA]:
        conn.execute("INSERT INTO Fasta VALUES(?, ?, ?)", (i[0], i[1], i[2]))
    for i in TABLECODES:
        conn.execute("INSERT INTO Codes VALUES(?, ?)", (i[0], i[1]))

    conn.commit()

 
def insertion(TABLECOMMENTS, TABLEDATES, TABLEFEATURES, TABLENAMES, TABLEFASTA, TABLECODES, TABLEPROTEIN, db_name, id_protein):
     conn = sqlite3.connect(db_name)
     delete(conn, id_protein)
     sqlite_generator(conn, TABLECOMMENTS, TABLEDATES, TABLEFEATURES, TABLENAMES, TABLEFASTA, TABLECODES, TABLEPROTEIN)
     
     conn.close()
 
 
