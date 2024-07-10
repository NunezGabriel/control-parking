# En este apartado podremos ver todos los menus como funciones las cuales se usan en todo el programa

# menu general
def menu():
    print("*------------------------------------------------------*")
    print("| BIENVENIDO AL SISTEMA DE CONTROL DEL ESTACIONAMIENTO |")
    print("*------------------------------------------------------*")
    print("| - Elije la opcion que quieras utilizar               |")
    print("|                                                      |")
    print("| 1) Administrar vehiculos                             |")
    print("| 2) Cobro de de cupo                                  |")
    print("| 3) Mostrar Lista                                     |")
    print("| 4) Buscar informacion del propietario                |")
    print("| 5) Papelera                                          |")
    print("| 6) Salir                                             |")
    print("*------------------------------------------------------*")

# mensaje de despedida al salir de la app
def mensajeDespedida():
    print("*---------------------------------------------------------*")
    print("| GRACIAS POR USAR EL SISTEMA DE CONTROL, HASTA PRONTO 👋 |")
    print("*---------------------------------------------------------*")


# menu de administracion de vehiculos
def menu_administrar():
    print("*------------------------------------------------------*")
    print("|             ADMINISTRACIÓN DE VEHÍCULOS              |")
    print("*------------------------------------------------------*")
    print("| - Elije la opcion que quieras utilizar               |")
    print("|                                                      |")
    print("| 1) Registrar vehículo                                |")
    print("| 2) Eliminar vehículo                                 |")
    print("| 3) Volver                                            |")
    print("*------------------------------------------------------*")

# menu de listado de vehiculos 
def menu_lista():
    print("*------------------------------------------------------*")
    print("|           LISTA DE VEHICULOS EN EL PARKING           |")
    print("*------------------------------------------------------*")
    print("| - Elije la opcion que quieras utilizar               |")
    print("| 1) Mostrar Lista                                     |")
    print("| 2) Buscar Vehiculo                                   |")
    print("| 3) Cancelar                                          |")
    print("*------------------------------------------------------*")

# menu de papelera 
def menu_papelera():
    print("*------------------------------------------------------*")
    print("|                    PAPELERA                          |")
    print("*------------------------------------------------------*")
    print("| - Elije la opcion que quieras utilizar               |")
    print("| 1) Restaurar Carro                                   |")
    print("| 2) Cancelar                                          |")
    print("*------------------------------------------------------*")

# menu de descuentos 
def menu_descuento():
    print("*------------------------------------------------------*")
    print("|           DESCUENTO POR REGISTRO DE VEHÍCULOS        |")
    print("*------------------------------------------------------*")
    print("| 1) Aplicar descuento                                 |")
    print("| 2) Volver al menú principal                          |")
    print("*------------------------------------------------------*")

def menuAforo():
    print("*------------------------------------------------------*")
    print("|                    FORO CARROS                       |")
    print("*------------------------------------------------------*")
    print("| 1) Establecer cantidad de carros en el foro          |")
    print("| 2) Ver espacio ocupado y disponible                  |")
    print("| 3) Salir al menú principal                           |")
    print("*------------------------------------------------------*")

def cobro_de_cupos_menu():
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