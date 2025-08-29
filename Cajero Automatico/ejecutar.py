from operaciones import Cuenta
from Menu import menu

def ejecutar():
    cuenta_personal = Cuenta(1400000)
    while True:
        opcion = menu()
        if opcion == "1":
            print(f"Su saldo es: {cuenta_personal.consultar()}")
        elif opcion == "2":
            try:
                cantidad = int(input("Ingrese la cantidad a depositar: "))
                if cuenta_personal.depositar(cantidad):
                    print("Depósito exitoso.")
                    print(f"Nuevo saldo: {cuenta_personal.consultar()}")
                else:
                    print("Monto inválido.")
            except ValueError:
                print("Por favor, ingrese un número válido.")
        elif opcion == "3":
            try:
                cantidad = int(input("Ingrese la cantidad a retirar: "))
                if cuenta_personal.retirar(cantidad):
                    print("Retiro exitoso.")
                    print(f"Nuevo saldo: {cuenta_personal.consultar()}")
                else:
                    print("Fondos insuficientes o monto inválido.")
            except ValueError:
                print("Por favor, ingrese un número válido.")
        elif opcion == "4":
            print("Gracias por usar el cajero automático.")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    ejecutar()