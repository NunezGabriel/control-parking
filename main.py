from globalResources import menu

while True:
    menu()
    opcion = input("Desea Continuar? Si/No: ")

    if opcion == "No":
        print("Adios :)")
        break
    else:
        continue

