# Importamos funciones y módulos necesarios
from vehicles_admin import vehiculos
from globalResources import menuAforo
import os

# Lista para almacenar los carros en el foro
foro_carros = []

def submenu_foro():
    # Declarar foro_carros como global para modificarla dentro de la función
    
    while True:
        # Mostrar el menú de aforo
        menuAforo()
        # Solicitar al usuario que seleccione una opción
        opcion = int(input("Seleccione una opción: "))
        os.system('cls')
        if opcion == 1:
            # Establecer la capacidad del foro
            cantidad_carros = int(input("Ingrese la cantidad de carros que puede tener el foro: "))
            foro_carros = [None] * cantidad_carros
            print(f"Foro establecido para {cantidad_carros} carros.")
        
        elif opcion == 2:
            os.system('cls')
            # Llenar el foro con los vehículos registrados y mostrar el espacio ocupado/disponible
            for i in range(min(len(vehiculos), len(foro_carros))):
                foro_carros[i] = vehiculos[i]
            
            # Calcular el espacio ocupado y disponible
            espacio_ocupado = len([carro for carro in foro_carros if carro is not None])
            espacio_disponible = len(foro_carros) - espacio_ocupado
            
            # Mostrar la información del espacio
            print(f"Espacio ocupado: {espacio_ocupado} carros")
            print(f"Espacio disponible: {espacio_disponible} carros")
        
        elif opcion == 3:
            os.system('cls')
            # Salir del submenu
            break
        
        else:
            # Mensaje de error para opciones inválidas
            print("Ingrese una opción válida.")