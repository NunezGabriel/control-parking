# Importamos funciones y módulos necesarios

from globalResources import menu_lista, menu_papelera 
from vehicles_admin import vehiculos, lista_papelera 
import os 

def buscarVehiculo():  # Creamos la funcion buscar vehiculo
    # Solicitamos al usuario que ingrese la placa del vehículo
    placa = input("Ingrese la placa del vehiculo a buscar xxx-xxx: ")

    # Verificamos si la lista de vehículos no está vacía
    if len(vehiculos) != 0:
        # Iteramos sobre cada vehículo en la lista
        for i in vehiculos:
            # Comprobamos si la placa ingresada coincide con la placa del vehículo actual
            if i["placa"] == placa:
                # Si se encuentra el vehículo, mostrar la información
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
                # Si no se encuentra el vehículo, mostrar mensaje de error
                print("🔴 Placa ingresada no existente")
    else:
        # Si la lista de vehículos está vacía, mostrar mensaje correspondiente
        print("🔴 No hay ningun vehiculo para mostrar")


def mostrarLi():
    # Imprimimos el título de la lista de vehículos
    print("#      LISTA DE VEHICULOS       #")
    
    # Verificamos si la lista de vehículos no está vacía
    if len(vehiculos) != 0:
        # Iteramos sobre cada vehículo en la lista
        for i in vehiculos:
            # Imprimimos la información de cada vehículo
            print("\n")
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
        # Si la lista de vehículos está vacía, mostrar mensaje correspondiente
        print("🔴 No hay ningun vehiculo para mostrar")

def restaurarMostrar():
    # Imprimimos el título de la lista de vehículos en la papelera
    print("#      LISTA PAPELERA       #")

    # Iteramos sobre cada vehículo en la lista de la papelera
    for i in lista_papelera:
        # Imprimimos la información de cada vehículo en la papelera
        print("\n")
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

    # Solicitar al usuario que ingrese la placa del vehículo a restaurar
    placa = input("Ingrese la placa a restuarar xxx-xxx: ")

    # Verificamos si la lista de la papelera no está vacía
    if len(lista_papelera) != 0:
        # Iteramos sobre cada vehículo en la lista de la papelera
        for i in lista_papelera:
            # Comprobar si la placa ingresada coincide con la placa del vehículo actual
            if i["placa"] == placa:
                # Si se encuentra el vehículo, restaurarlo a la lista principal
                vehiculos.append(i)
                print("🟢 Vehiculo restaurado correctamente")
            else:
                # Si no se encuentra el vehículo, mostrar mensaje de error
                # Nota: Este 'else' debería estar fuera del bucle para evitar múltiples mensajes
                print("🔴 Placa ingresada no existente")
    else:
        # Si la lista de la papelera está vacía, mostrar mensaje correspondiente
        print("🔴 No hay ningun vehiculo para mostrar")

def mostrar_lista():
    while True:
        # Mostrar el menú de lista
        menu_lista()
        # Solicitar al usuario que ingrese una opción
        opcion = int(input("Ingrese un numero de opcion valido: "))
        
        if opcion == 1:
            # Limpiar la pantalla
            os.system('cls')
            # Mostrar la lista de vehículos
            mostrarLi()
        elif opcion == 2:
            # Limpiar la pantalla
            os.system('cls')
            # Buscar un vehículo específico
            buscarVehiculo()
        elif opcion == 3:
            # Salir del bucle y volver al menú principal
            break
        else:
            # Mensaje de error si la opción no es válida
            print("🔴 Ingrese un numero VALIDO")
            continue

def papelera():
    while True:
        # Mostrar el menú de la papelera
        menu_papelera()
        # Solicitar al usuario que ingrese una opción
        opcion = int(input("Ingrese un numero de opcion valido: "))
        if opcion == 1:
            # Limpiar la pantalla
            os.system('cls')
            # Mostrar y permitir restaurar vehículos de la papelera
            restaurarMostrar()
        elif opcion == 2:
            # Salir del bucle y volver al menú principal
            break
        else:
            # Mensaje de error si la opción no es válida
            print("🔴 Ingrese un numero VALIDO")
            continue
