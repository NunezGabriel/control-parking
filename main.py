# Importamos funciones y módulos necesarios
from globalResources import menu, mensajeDespedida
from lista_papelera import mostrar_lista, papelera
from vehicles_admin import administrar_vehiculos
from info_prop import submenu_foro
import os

# Bucle principal del programa
while True:
    # Mostrar el menú principal
    menu()
    # Solicitar al usuario que ingrese una opción
    opcion = int(input("Ingrese un numero de opcion valido: "))

    if opcion == 1:
        # Limpiar la pantalla
        os.system('cls')
        # Ir al módulo de administración de vehículos
        administrar_vehiculos()
    elif opcion == 2:
        # Limpiar la pantalla
        os.system('cls')
        # Mostrar mensaje de despedida y salir del programa
        mensajeDespedida()
        break
    elif opcion == 3:
        # Limpiar la pantalla
        os.system('cls')
        # Mostrar la lista de vehículos
        mostrar_lista()
    elif opcion == 4:
        # Limpiar la pantalla
        os.system('cls')
        # Ir al submenu del foro
        submenu_foro()
    elif opcion == 5:
        # Limpiar la pantalla
        os.system('cls')
        # Ir a la papelera
        papelera()
    elif opcion == 6:
        # Limpiar la pantalla
        os.system('cls')
        # Mostrar mensaje de despedida y salir del programa
        mensajeDespedida()
        break
    else:
        # Mensaje de error si la opción no es válida
        print("Ingrese un numero VALIDO")
        continue
