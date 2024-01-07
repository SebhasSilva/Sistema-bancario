#Ejercicio sistema bancario

class SistemaBancario:
    def __init__(self):
        self.username = "Admin"
        self.password = "Contraseña321"
        self.intentos_fallidos = 0
        self.saldo = 2000
        self.cuenta_bloqueada = False

    def iniciar_sesion(self):
        while not self.cuenta_bloqueada:
            username_input = input("Ingrese su nombre de usuario: ")
            password_input = input("Ingrese su contraseña: ")

            if username_input == self.username and password_input == self.password:
                return True
            else:
                self.intentos_fallidos += 1
                print("Credenciales incorrectas. Intentos fallidos:", self.intentos_fallidos)
                
                if self.intentos_fallidos == 3:
                    print("Cuenta bloqueada. Contacte al servicio al cliente.")
                    self.cuenta_bloqueada = True
                    return False

    def depositar(self, cantidad):
        if not self.cuenta_bloqueada:
            if cantidad > 0:
                self.saldo += cantidad
                print(f"Depósito exitoso. Nuevo saldo: ${self.saldo}")
            else:
                print("Ingrese una cantidad válida para depositar.")
        else:
            print("Cuenta bloqueada. No se pueden realizar transacciones.")

    def retirar(self, cantidad):
        if not self.cuenta_bloqueada:
            if cantidad > 0 and cantidad <= self.saldo:
                self.saldo -= cantidad
                print(f"Retiro exitoso. Nuevo saldo: ${self.saldo}")
            else:
                print("Fondos insuficientes o cantidad no válida para retirar.")
        else:
            print("Cuenta bloqueada. No se pueden realizar transacciones.")

    def ver_saldo(self):
        if not self.cuenta_bloqueada:
            print(f"Saldo actual: ${self.saldo}")
        else:
            print("Cuenta bloqueada. No se pueden realizar transacciones.")

    def transferir(self, destinatario, cantidad):
        if not self.cuenta_bloqueada:
            if cantidad > 0 and cantidad <= self.saldo:
                self.saldo -= cantidad
                destinatario.depositar(cantidad)
                print(f"Transferencia exitosa. Nuevo saldo: ${self.saldo}")
            else:
                print("Fondos insuficientes o cantidad no válida para transferir.")
        else:
            print("Cuenta bloqueada. No se pueden realizar transacciones.")


# Ejemplo de uso
usuario1 = SistemaBancario()

# Intentos de inicio de sesión
if usuario1.iniciar_sesion():
    usuario1.ver_saldo()
    usuario1.depositar(500)
    usuario1.ver_saldo()
    usuario1.retirar(300)
    usuario1.ver_saldo()

    # Crear otro usuario
    usuario2 = SistemaBancario()

    # Transferencia entre usuarios
    usuario1.transferir(usuario2, 200)
    usuario1.ver_saldo()
    usuario2.ver_saldo()
