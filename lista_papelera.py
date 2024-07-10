from globalResources import menu_lista, menu_papelera
from vehicles_admin import vehiculos, lista_papelera
import os

def buscarVehiculo():
    placa = input("Ingrese la placa del vehiculo a buscar xxx-xxx: ")
    
    if len(vehiculos) != 0:
        for i in vehiculos:
            if i["placa"] == placa:
                print("🟢 Vehiculo encontrado")
                print("O=====================================O")
                print(f"Nro de placa del vehiculo: {i["placa"]}")
                print(f"Nombre del Propietario: {i["propietario"]}")
                print(f"Tipo de vehiculo: {i["tipo"]}")
                print(f"Modelo de vehiculo: {i["modelo_vehiculo"]}")
                print(f"Marca de vehiculo: {i["marca_vehiculo"]}")
                print(f"Tiene reserva: {i["reserva"]}")
                print(f"Hora de entrada del vehiculo: {i["hora_entrada"]}")
                print("O=====================================O \n")
                print("\n")
            else:
                print("🔴 Placa ingresada no existente")
    else:
        print("🔴 No hay ningun vehiculo para mostrar")    



def mostrar_lista():
    while True:
        menu_lista()
        opcion = int(input("Ingrese un numero de opcion valido: "))
        if opcion == 1:
            os.system('cls')
            buscarVehiculo()
        elif opcion == 2:
            break
        else:
            print("🔴 Ingrese un numero VALIDO")
            continue

def papelera():
    while True:
        menu_papelera()
        opcion = int(input("Ingrese un numero de opcion valido: "))
        if opcion == 1:
            os.system('cls')
            print("restaurando ...")
        elif opcion == 2:
            break
        else:
            print("🔴 Ingrese un numero VALIDO")
            continue
