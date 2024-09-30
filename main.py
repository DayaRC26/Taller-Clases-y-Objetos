from Modelo import Cuenta
import UI

cuenta_clientes = []

def crear_cuenta():
    numero_cuenta, dni, nombre_cliente, saldo = UI.solicitar_datos_cuenta()
    nueva_cuenta = Cuenta(numero_cuenta, dni, nombre_cliente, saldo)
    cuenta_clientes.append(nueva_cuenta)
    print("Cuenta creada exitosamente.\n")

def opcion_depositar_dinero():
    if cuenta_clientes:
        dinero = UI.solicitar_dinero()
        cuenta_clientes[0].depositar_dinero(dinero)  
        print("Depósito realizado con éxito.\n")
    else:
        print("No hay cuentas registradas.")

def opcion_retirar_dinero():
    if cuenta_clientes:
        dinero = UI.solicitar_dinero()
        cuenta_clientes[0].retirar_dinero(dinero)  
        print("Retiro realizado con éxito.")
    else:
        print("No hay cuentas registradas.\n")


while True:
    UI.mostrar_menu()
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        crear_cuenta()
        
    elif opcion == 2:
        opcion_depositar_dinero()
        
    elif opcion == 3:
        opcion_retirar_dinero()
        
    elif opcion == 4:
        UI.mostrar_cuentas(cuenta_clientes)
        
    elif opcion == 5:
        print("\nGracias por usar la aplicación, hasta pronto...")
        break
        
    else:
        print("\nOpción no válida. Ingresa una nueva opción.\n")

