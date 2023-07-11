import core
import os
dictPartici =  {"data":[]}

def LoadInfoParticipantes():
    global dictPartici
    if (core.checkFile("participantes.json")):
        dictPartici = core.LoadInfo("participantes.json")
    else:
        core.crearInfo("Participantes.json",dictPartici)

def Mainmenu():
    os.system('clear')
    isMenuPart = True
    print("1. Registrar")
    print("2. Buscar participante")
    print("3. Editar participante")
    print("4. Eliminar participante")
    print("5. Regresar menu principal")
    opcion = int(input(">"))
    if (opcion == 1):
        datos = {}
        data  ={
            "id": input("Ingrese la Id del Participante : ").capitalize(),
            "nombre": input("Ingrese el nombre del participante : ").capitalize(),
            "Apellido": input("Ingrese el apellido del participante : ").capitalize(),
            "Edad": int((input("Ingrese la edad del participante: "))),
            "correo" : input("Ingrese el correo electronico: ").capitalize(),
            "cuidad" : input("Ingrese la cuidad de origen:  ").capitalize(),
            "estado" : input("Ingrese el estado civil: ").capitalize(),
            "genero" : input("Ingrese el genero: ").capitalize(),
            "telefono" : input("Ingrese el numero de telefono: ")
        
    if (data["Edad"]>18):
       pass
        }
        dictPartici["data"].append(data)
        core.crearInfo("parcipantes.json",data)
    elif (opcion == 2 ):
        pass
    elif (opcion == 3):
        pass
    elif (opcion == 4):
        pass    
    elif (opcion == 5):
        isMenuPart = False
    if (isMenuPart):
        Mainmenu()    