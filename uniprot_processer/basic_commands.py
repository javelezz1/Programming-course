# module 3
import sys

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
