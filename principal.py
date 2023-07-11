import os
import json
import participantes


if __name__=="__main__":
    isActive = True
    opcion = 0
    while isActive:
        os.system('clear')
        print('+','-'*55,'+')
        print("|{:^20}{}{:^30}|".format(' ','Menu ',' '))
        print('+','-'*55,'+')
        print("1. Registro de Participantes")
        print("2. Lista de participantes")
        print("3. Edicion de participantes")        
        print("4. Eliminacion de participantes")
        print("5. Salir del programa...")
        opcion = int(input(">"))
        if (opcion == 1):
            participantes.LoadInfoParticipantes()
            participantes.Mainmenu()
        elif (opcion == 2):
            pass
        elif (opcion == 3):
            pass
        elif (opcion == 4):
            pass
        elif (opcion == 5):
            isActive = False
            print("=====Adios======")