import datetime

diccionarioxDia = {}        # Se guardan las visitas
historialVisitas = {}       # Para enlazar con el verdadero historial
estadoDescuento = {}        # Si se usaron descuentos (cupos)


def calcular_descuento(visitas):
    return (visitas // 5) * 0.10


while True:
    En_Sa = input("1-Entrada\t2-Salida\t3-Descuentos\t4-Atrás\n--> ")
    if En_Sa == "4":
        break

    cobroxHora = 2.00
    descuento = 0

    if En_Sa == "1":
        Cliente = input("Ingrese su número de DNI: ")
        Entrada = datetime.datetime.now()
        diccionarioxDia[Cliente] = Entrada
        if Cliente in historialVisitas:
            historialVisitas[Cliente] += 1
        else:
            historialVisitas[Cliente] = 1
            estadoDescuento[Cliente] = "no aplicado"

    elif En_Sa == "2":
        buscarDNI = input("Ingrese su número de DNI: ")
        if buscarDNI in diccionarioxDia:
            Salida = datetime.datetime.now()
            tiempodeEntrada = diccionarioxDia[buscarDNI]
            tiempoTotal = Salida - tiempodeEntrada
            totalSegundos = tiempoTotal.total_seconds()
            totalHoras = (totalSegundos // 30)
            cobroTotal = totalHoras * cobroxHora

            if buscarDNI in historialVisitas:
                visitas = historialVisitas[buscarDNI]
                if visitas >= 5 and estadoDescuento[buscarDNI] == "no aplicado":
                    descuento = calcular_descuento(visitas)
                    cobroTotal -= cobroTotal * descuento
                    estadoDescuento[buscarDNI] = "aplicado"

            boleta = (
                "============================\n"
                "         BOLETA DE PAGO        \n"
                "============================\n"
                f"DNI del Cliente: {buscarDNI}\n"
                f"Hora de Entrada: {tiempodeEntrada}\n"
                f"Hora de Salida:  {Salida}\n"
                f"Tiempo Total:    {int(totalHoras)} horas\n"
                f"Descuento:       {descuento * 100}%\n"
                f"Cobro Total:     S/ {cobroTotal:.2f}\n"
                "============================\n"
            )

            archivo = open("boleta.txt", "a")
            archivo.write(boleta)
            archivo.close()

            print(boleta)
            del diccionarioxDia[buscarDNI]

        else:
            print("No ha ingresado todavía")

    elif En_Sa == "3":
        DNI_descuentos = input("Ingrese su número de DNI: ")
        if DNI_descuentos in historialVisitas:
            num_rep_DNI = historialVisitas[DNI_descuentos]
            if num_rep_DNI >= 5 and estadoDescuento[DNI_descuentos] == "no aplicado":
                descuento = calcular_descuento(num_rep_DNI)
                print(f"Tiene un descuento de: {descuento * 100}%")
            elif estadoDescuento[DNI_descuentos] == "aplicado":
                print("El descuento ya ha sido aplicado y no es válido nuevamente.")
            else:
                print("No tiene suficientes visitas para un descuento")
        else:
            print("No se encontraron registros de visitas para este DNI")

    else:
        print("La opción no es válida, inténtelo nuevamente")
