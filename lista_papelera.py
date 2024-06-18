from globalResources import menu_lista, menu_papelera

def mostrar_lista():
    while True:
        print("*------------------------------------------------------*")
        print("|           LISTA DE VEHICULOS EN EL PARKING           |")
        print("*------------------------------------------------------*")
        menu_lista()
        opcion = int(input("Ingrese un numero de opcion valido: "))
        if opcion == 1:
            print("buscando ...")
        elif opcion == 2:
            break
        else:
            print("Ingrese un numero VALIDO")
            continue

def papelera():
    while True:
        print("*------------------------------------------------------*")
        print("|                    PAPELERA                          |")
        print("*------------------------------------------------------*")
        menu_papelera()
        opcion = int(input("Ingrese un numero de opcion valido: "))
        if opcion == 1:
            print("restaurando ...")
        elif opcion == 2:
            break
        else:
            print("Ingrese un numero VALIDO")
            continue
