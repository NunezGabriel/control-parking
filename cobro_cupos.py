import datetime, globalResources as glbR, vehicles_admin as va

diccionarioxDia = {}        # Se guardan las visitas
historialVisitas = {}       # Para enlazar con el verdadero historial
estadoDescuento = {}        # Si se usaron descuentos (cupos)


def calcular_descuento(visita):         # Por cada 5 visitas, se le da un descuento del 10%
    return (visita // 5) * 0.10


def cobro_de_cupos():
    print("*------------------------------------------------------*")
    print("|                    COBRO DE CUPOS                    |")
    print("*------------------------------------------------------*")
    print("| - Elije la opcion que quieras utilizar               |")
    print("|                                                      |")
    print("| 1) Entrada                                           |")
    print("| 2) Salida                                            |")
    print("| 3) Descuentos                                        |")
    print("| 4) Atrás                                             |")
    print("*------------------------------------------------------*")


cobro_de_cupos()


while True:
    En_Sa = input("--> ")
    cobroxHora = 2.00
    descuento = 0
    if En_Sa == "4":            # Retrocede al menú
        glbR.menu()

    if En_Sa == "1":
        placa = va.registrar_vehiculo()            # De vehicles_admin
        Entrada = datetime.datetime.now()
        diccionarioxDia[placa] = Entrada            # Guarda la entrada
        if placa in historialVisitas:
            historialVisitas[placa] += 1            # Aumenta el historial de visitas
        else:
            historialVisitas[placa] = 1             # Primera visita
            estadoDescuento[placa] = "no aplicado"  # no hay suficiente para solicitar un descuento

    elif En_Sa == "2":
        buscarPlaca = input("Ingrese su número de placa: ")
        if buscarPlaca in diccionarioxDia:                  # Busca la placa donde se registró
            Salida = datetime.datetime.now()                # Guarda la salida
            tiempodeEntrada = diccionarioxDia[buscarPlaca]  # Guarda el tiempo de entrada en otra variable
            tiempoTotal = Salida - tiempodeEntrada          # Se calcula el tiempo que se estuvo dentro
            totalSegundos = tiempoTotal.total_seconds()     # Se calcula el tiempo total en segundos
            totalHoras = (totalSegundos // 30)              # Cada 30 segundos es 1 hora
            cobroTotal = totalHoras * cobroxHora            # Se calcula cuánto corresponde cobrar por el tiempo

            if buscarPlaca in historialVisitas:
                visitas = historialVisitas[buscarPlaca]         # Se saca la cantidad de visitas registrado
                if visitas >= 5 and estadoDescuento[buscarPlaca] == "no aplicado":
                    descuento = calcular_descuento(visitas)     # Se calcula el descuento
                    cobroTotal -= cobroTotal * descuento
                    estadoDescuento[buscarPlaca] = "aplicado"   # Ya no se puede usar el descuento

                    # Boleta:
            boleta = (
                "============================\n"
                "         BOLETA DE PAGO        \n"
                "============================\n"
                f"Placa del auto: {buscarPlaca}\n"
                f"Hora de Entrada: {tiempodeEntrada}\n"
                f"Hora de Salida:  {Salida}\n"
                f"Tiempo Total:    {int(totalHoras)} horas\n"
                f"Descuento:       {descuento * 100}%\n"
                f"Cobro Total:     S/ {cobroTotal:.2f}\n"
                "============================\n"
            )

            # Guarda la boleta
            archivo = open("boleta.txt", "a")
            archivo.write(boleta)
            archivo.close()

            # Se imprime la boleta
            print(boleta)
            # Se elimina el registro de entrada para una próxima
            del diccionarioxDia[buscarPlaca]

        else:
            print("No ha ingresado todavía")

    elif En_Sa == "3":
        Placa_descuentos = input("Ingrese su número de placa: ")
        if Placa_descuentos in historialVisitas:                        # Busca la placa en el historial
            num_rep_Placa = historialVisitas[Placa_descuentos]          # Número de repeticiones
            if num_rep_Placa >= 5 and estadoDescuento[Placa_descuentos] == "no aplicado":
                descuento = calcular_descuento(num_rep_Placa)           # Calcula el descuento
                print(f"Tiene un descuento de: {descuento * 100}%")
            elif estadoDescuento[Placa_descuentos] == "aplicado":
                print("El descuento ya ha sido aplicado y no es válido nuevamente.")
            else:
                print("No tiene suficientes visitas para un descuento")
        else:
            print("No se encontraron registros de visitas para este número de placa")

    else:
        print("La opción no es válida, inténtelo nuevamente")
