from vehicles_admin import vehiculos

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
