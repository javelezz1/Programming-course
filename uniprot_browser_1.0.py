
# Made by Jhon


import sys
import os

#Errores de que faltan datos

if len(sys.argv) == 1:
    print("Filename not provided")
    exit()
elif len(sys.argv) == 2:
    print("Query not given")
    exit()
    
  #Se ponen los inputs de la terminal en variables

dato = sys.argv[2].split(".contains.")
string=dato[1]
query = dato[0]
fields= sys.argv[3:]
archivo = sys.argv[1]

# Si el archivo no existe

boolean=os.path.isfile(archivo)

if boolean == False:
    print("The file given does no exist")
    exit()
  
#Funcion principal



def procesar(file, string, query, fields):
  matches=0
  total_processed=0
  record=[]
  
  while True:
    line=file.readline()  
    # Este if es para leer el archivo una proteina a la vez.
    if line.startswith("ID"):
      total_processed +=1
      record.clear()
      record=[line[:-1]]
    elif line.startswith("//"):
      # Si ya terminamos de leer y registrar ese bloque en record, volvemos a leer ese 
      # bloque para ver si nos interesa.
      for i in record: 
        # Si alguna linea coincide con el query, tomamos los datos que necesitamos 
        # y los imprimimos.  
        if string in i and i.startswith(query):
          matches += 1
          if len(sys.argv) == 3:
            for k in record:
                print(k)
            print("No fields asked for, all fields presented")
            break
          for j in record:
            if j[:2] in fields:
              print(j)
            if j[:2] == "  " and "SQ" in fields:
              print(j) 
          break
    else:
      record.append(line[:-1])
    if not line:
      break
  return total_processed, matches

    
file = open(archivo, "rt")
#lines=file.readlines()



total_processed, matches = procesar(file, string, query, fields)
file.close()


print("Match records ", matches)
print("Records processed ", total_processed)
