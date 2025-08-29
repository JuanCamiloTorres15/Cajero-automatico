class Cuenta:
    def __init__(self, saldo=0):
        self.saldo = saldo
    def consultar(self):
        return self.saldo
    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            return True
        return False
    def retirar(self, monto):
        if 0 < monto <= self.saldo:
            self.saldo -= monto
            return True
        return False