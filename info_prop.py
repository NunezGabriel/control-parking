from vehicles_admin import vehiculos
from globalResources import menu_administrar, menu_descuento
import os

def aplicar_descuento():
    propietario = input("Ingrese el nombre del propietario para aplicar descuento: ")
    contador = 0
    for vehiculo in vehiculos:
        if vehiculo["propietario"] == propietario:
            contador += 1
    if contador >= 3:
        print(f"Se aplicó un descuento del 20% al propietario {propietario}.")
    else:
        print(f"No se aplicó descuento. {propietario} solo tiene {contador} vehículos registrados.")

def submenu_descuento():
    while True:
        menu_descuento()
        opcion = int(input("Ingrese un número de opción válido: "))
        if opcion == 1:
            os.system('cls')
            aplicar_descuento()
        elif opcion == 2:
            break
        else:
            print("Opción no válida. Intente de nuevo.")