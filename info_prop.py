from vehicles_admin import vehiculos
from globalResources import menu_administrar, menu_descuento
import os

foro_carros = []
def submenu_foro():
    global foro_carros
    while True:
        print("*------------------------------------------------------*")
        print("|           FORO CARROS                                |")
        print("*------------------------------------------------------*")
        print("| 1) Establecer cantidad de carros en el foro          |")
        print("| 2) Ver espacio ocupado y disponible                  |")
        print("| 3) Salir al menú principal                           |")
        print("*------------------------------------------------------*")

        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            cantidad_carros = int(input("Ingrese la cantidad de carros que puede tener el foro: "))
            foro_carros = [None] * cantidad_carros
            print(f"Foro establecido para {cantidad_carros} carros.")
        elif opcion == 2:
            for i in range(min(len(vehiculos), len(foro_carros))):
                foro_carros[i] = vehiculos[i]
            espacio_ocupado = len([carro for carro in foro_carros if carro is not None])
            espacio_disponible = len(foro_carros) - espacio_ocupado
            print(f"Espacio ocupado: {espacio_ocupado} carros")
            print(f"Espacio disponible: {espacio_disponible} carros")
        elif opcion == 3:
            break
        else:
            print("Ingrese una opción válida.")