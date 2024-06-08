from globalResources import menu, mensajeDespedida

while True:
    menu()
    opcion = int(input("Ingrese un numero de opcion valido: "))

    if opcion == 5:
        mensajeDespedida()
        break
    else:
        continue

