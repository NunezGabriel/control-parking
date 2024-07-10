from globalResources import menu, mensajeDespedida
from lista_papelera import mostrar_lista, papelera
from vehicles_admin import administrar_vehiculos
from info_prop import submenu_foro
import os


while True:
    menu()
    opcion = int(input("Ingrese un numero de opcion valido: "))

    if opcion == 1:
        os.system('cls')
        administrar_vehiculos()
    elif opcion == 2:
        os.system('cls')
        mensajeDespedida()
        break
    elif opcion == 3:
        os.system('cls')
        mostrar_lista()
    elif opcion == 4:
        os.system('cls')
        submenu_foro()
    elif opcion == 5:
        os.system('cls')
        papelera()
    elif opcion == 6:
        os.system('cls')
        mensajeDespedida()
        break
    else:
        print("Ingrese un numero VALIDO")
        continue

