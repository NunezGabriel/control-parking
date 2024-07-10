# Importamos funciones y módulos necesarios
from globalResources import menu_administrar
from datetime import datetime
import os

# Lista para almacenar los vehículos
vehiculos = []

def registrar_vehiculo():
    while True:
        # Solicitar y validar la placa del vehículo
        placa = input("Ingrese la placa del vehículo: ")
        if len(placa) == 7 and placa[3] == "-":
            print("🟢 Placa registrada correctamente.")
            break
        else:
            print("🔴 Error: La placa fue ingresada incorrectamente.")
    
    # Solicitar información adicional del vehículo
    propietario = input("Ingrese el nombre del propietario: ")
    tipo = input("Ingrese el tipo de vehículo: ")
    modelo_vehiculo = input("Ingrese el modelo del vehículo: ")
    marca_vehiculo = input("Ingrese la marca  del vehículo: ")
    reserva = input("Tiene reserva? (si/no): ")
    hora_entrada = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Crear un diccionario con la información del vehículo
    vehiculo = {
        "placa": placa,
        "propietario": propietario,
        "tipo": tipo,
        "modelo_vehiculo": modelo_vehiculo,
        "marca_vehiculo": marca_vehiculo,
        "reserva": reserva,
        "hora_entrada": hora_entrada,
    }

    # Agregar el vehículo a la lista
    vehiculos.append(vehiculo)
    print("🟢 Vehículo registrado exitosamente.")

# Lista para almacenar vehículos eliminados
lista_papelera = []

def eliminar_vehiculo():
    # Solicitar la placa del vehículo a eliminar
    placa = input("Ingrese la placa del vehículo a eliminar: ")
    for vehiculo in vehiculos:
        if vehiculo["placa"] == placa:
            # Remover el vehículo de la lista principal y agregarlo a la papelera
            vehiculos.remove(vehiculo)
            lista_papelera.append(vehiculo)
            print("🟢 Vehículo eliminado exitosamente.")
            return
    print("🔴 Error: Vehículo no encontrado.")

def administrar_vehiculos():
    while True:
        # Mostrar el menú de administración
        menu_administrar()
        opcion = int(input("Ingrese un número de opción válido: "))
        if opcion == 1:
            # Limpiar la pantalla
            os.system('cls')
            registrar_vehiculo()
        elif opcion == 2:
            # Limpiar la pantalla
            os.system('cls')
            eliminar_vehiculo()
        elif opcion == 3:
            os.system('cls')
            break
        else:
            print("🔴 Opción no válida. Intente de nuevo.")
