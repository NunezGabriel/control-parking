from globalResources import menu, mensajeDespedida
from lista_papelera import mostrar_lista, papelera
from vehicles_admin import administrar_vehiculos

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
        mensajeDespedida()
        break
    elif opcion == 5:
        papelera()
    elif opcion == 6:
        mensajeDespedida()
        break
    else:
        print("Ingrese un numero VALIDO")
        continue

