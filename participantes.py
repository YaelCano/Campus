import core
import os
dictPartici =  {"data":[]}

def LoadInfoParticipantes():
    global dictPartici
    if (core.checkFile("campers.json")):
        dictPartici = core.LoadInfo("campers.json")
    else:
        core.crearInfo("campers.json",dictPartici)

def Mainmenu():
    os.system('clear')
    isMenuPart = True
    print("1. Registrar")
    
    opcion = int(input(">"))
    if (opcion == 1):
        
        datos  ={
            "id": input("Ingrese la Id del Participante : ").capitalize(),
            "nombre": input("Ingrese el nombre del participante : ").capitalize(),
            "Apellido": input("Ingrese el apellido del participante : ").capitalize(),
            "Edad": int((input("Ingrese la edad del participante: "))),
            "correo" : input("Ingrese el correo electronico: ").capitalize(),
            "cuidad" : input("Ingrese la cuidad de origen:  ").capitalize(),
            "estado" : input("Ingrese el estado civil: ").capitalize(),
            "genero" : input("Ingrese el genero: ").capitalize(),
            "telefono" : input("Ingrese el numero de telefono: ")
        }
    if (datos["Edad"]<18):
        acudiente ={
         "id_acudiente": input("Ingrese la id del acudiente: ").capitalize(),
         "nombre_acu":input("Ingrese el nombre del acudinete: ").capitalize(),
         "parentesco":input("Ingrese el parentesco: ") 
        }
        datos["acudiente"] = acudiente
        dictPartici["datos"].append(datos)
        core.crearInfo("campers.json",datos)
    else:
        dictPartici["datos"].append(datos)
        core.crearInfo("camprs.json",datos)
 