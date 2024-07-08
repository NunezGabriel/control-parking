from globalResources import menu_administrar
from datetime import datetime

vehiculos = []
def registrar_vehiculo():
    while True:
        placa = input("Ingrese la placa del vehículo: ")
        if len(placa) == 7 and placa[3] == "-":
            print("Placa registrada correctamente.")
            break
        else:
            print("Error: La placa fue ingresada incorrectamente.")
    propietario = input("Ingrese el nombre del propietario: ")
    tipo = input("Ingrese el tipo de vehículo: ")
    modelo_vehiculo = input("Ingrese el modelo del vehículo: ")
    marca_vehiculo = input("Ingrese la marca  del vehículo: ")
    reserva = input("Tiene reserva? (si/no): ")
    hora_entrada = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    vehiculo = {
        "placa": placa,
        "propietario": propietario,
        "tipo": tipo,
        "modelo_vehiculo": modelo_vehiculo,
        "marca_vehiculo": marca_vehiculo,
        "reserva": reserva,
        "hora_entrada": hora_entrada,
    }

    vehiculos.append(vehiculo)
    print("Vehículo registrado exitosamente.")

lista_papelera = []
def eliminar_vehiculo():
    placa = input("Ingrese la placa del vehículo a eliminar: ")
    for vehiculo in vehiculos:
        if vehiculo["placa"] == placa:
            vehiculos.remove(vehiculo)
            lista_papelera.append(vehiculo)
            print("Vehículo eliminado exitosamente.")
            return
    print("Error: Vehículo no encontrado.")

def administrar_vehiculos():
    while True:
        menu_administrar()
        opcion = int(input("Ingrese un número de opción válido: "))
        if opcion == 1:
            registrar_vehiculo()
        elif opcion == 2:
            eliminar_vehiculo()
        elif opcion == 3:
            break
        else:
            print("Opción no válida. Intente de nuevo.")
