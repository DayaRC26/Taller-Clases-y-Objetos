from Modelo import Cuenta
import UI

cuenta_clientes = []

def crear_cuenta():
    numero_cuenta, dni, nombre_cliente, saldo = UI.solicitar_datos_cuenta()
    nueva_cuenta = Cuenta(numero_cuenta, dni, nombre_cliente, saldo)
    cuenta_clientes.append(nueva_cuenta)
    print("Cuenta creada exitosamente.\n")

def guardar_numero_cuenta():
    return int(input("Ingresa el número de cuenta: "))

def buscar_cuenta(numero_cuenta):
    for cuenta in cuenta_clientes:
        if cuenta.numero_cuenta == numero_cuenta:
            return cuenta
    return None

def opcion_depositar_dinero(numero_cuenta):
    cuenta = buscar_cuenta(numero_cuenta)
    if cuenta_clientes:
        if cuenta:
            dinero = UI.solicitar_dinero()
            cuenta.depositar_dinero(dinero)  
            print("Depósito realizado con éxito.\n")
        else:
            print("Cuenta inexistente.")
    else:
        print("No hay cuentas registradas.")

def opcion_retirar_dinero(numero_cuenta):
    cuenta = buscar_cuenta(numero_cuenta)
    if cuenta_clientes:
        if cuenta:
            dinero = UI.solicitar_dinero()
            cuenta.retirar_dinero(dinero)  
            print("Retiro realizado con éxito.\n")
        else:
            print("Cuenta inexistente.")
    else:
        print("No hay cuentas registradas.")


while True:
    UI.mostrar_menu()
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        crear_cuenta()
        
    elif opcion == 2:
        opcion_depositar_dinero(guardar_numero_cuenta())
        
    elif opcion == 3:
        opcion_retirar_dinero(guardar_numero_cuenta())
        
    elif opcion == 4:
        UI.mostrar_cuentas(cuenta_clientes)
        
    elif opcion == 5:
        print("\nGracias por usar la aplicación, hasta pronto...")
        break
        
    else:
        print("\nOpción no válida. Ingresa una nueva opción.\n")

