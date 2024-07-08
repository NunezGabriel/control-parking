from globalResources import menu, mensajeDespedida
from lista_papelera import mostrar_lista, papelera
<<<<<<< HEAD
from vehicles_admin import registrar_vehiculo, eliminar_vehiculo
from globalResources import menu_administrar, menu_descuento
from info_prop import aplicar_descuento
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
def submenu_descuento():
    while True:
        menu_descuento()
        opcion = int(input("Ingrese un número de opción válido: "))
        if opcion == 1:
            aplicar_descuento()
        elif opcion == 2:
            break
        else:
            print("Opción no válida. Intente de nuevo.")
=======
from vehicles_admin import administrar_vehiculos

>>>>>>> 680e509636275c4bd16656144eda0ec4b1923b80
while True:
    menu()
    opcion = int(input("Ingrese un numero de opcion valido: "))

    if opcion == 1:
        administrar_vehiculos()
    elif opcion == 2:
        mensajeDespedida()
        break
    elif opcion == 3:
        mostrar_lista()
    elif opcion == 4:
        submenu_descuento()
    elif opcion == 5:
        papelera()
    elif opcion == 6:
        mensajeDespedida()
        break
    else:
        print("Ingrese un numero VALIDO")
        continue

