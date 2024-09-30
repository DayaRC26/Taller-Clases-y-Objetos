class Cuenta:
    def __init__(self, numero_cuenta, dni, nombre_cliente, saldo):
        self.numero_cuenta = numero_cuenta
        self.dni = dni
        self.nombre_cliente = nombre_cliente
        self.saldo = saldo

    def depositar_dinero(self, dinero):
        retencion = dinero * 0.19
        self.saldo += dinero - retencion
    
    def retirar_dinero(self, dinero):
        if dinero <= self.saldo:
            self.saldo -= dinero
        else:
            print("Saldo Insuficiente")

    def mostrar_datos_cuenta(self):
        print("\nNúmero de cuenta: ", self.numero_cuenta)
        print("Documento de identidad: ", self.dni)
        print("Nombre del Cliente: ", self.nombre_cliente)
        print("Saldo: ", self.saldo)

