def mostrar_menu():
    print("\n~ Cuenta Bancaria ~")
    print("1. Crear cuenta")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Mostrar todas las cuentas")
    print("5. Salir")

def solicitar_datos_cuenta():
    numero_cuenta = int(input("Ingrese el número de cuenta: "))
    documento_id = int(input("Ingrese el número documento de identidad: "))
    nombre = input("Ingrese el nombre del cliente: ")
    saldo = float(input("Ingrese el saldo: "))
    return numero_cuenta, documento_id, nombre, saldo

def mostrar_cuentas(cuentaClientes):
    if not cuentaClientes:
        print("No hay cuentas registradas.\n")
    else:
        for cuenta in cuentaClientes:
            print(cuenta.mostrar_datos_cuenta())

def solicitar_dinero():
    dinero = float(input("Ingrese el dinero: "))
    return dinero