class Conta:
    def __init__(self, saldo):
        self._saldo = saldo

    @property #get
    def saldo(self):
        return self._saldo
    
    @saldo.setter #set
    def saldo(self, valor):
        self._saldo = valor
    
    def sacar(self, valor):
        self.saldo-=valor
    
    def depositar(self, valor):
        self.saldo+=valor

class Corrente(Conta):
    def __init__(self, saldo):
        super().__init__(saldo)

class Poupanca(Conta):
    def __init__(self, saldo):
        super().__init__(saldo)


cc1 = Corrente(1000)
print("Conta Corrente")
print(f"Saldo atual R$ {cc1.saldo:.2f}")
cc1.sacar(100)
print(f"Saldo após saque R$ {cc1.saldo:.2f}")
cc1.depositar(100)
print(f"Saldo após depósito R$ {cc1.saldo:.2f}")

print("\n")

cp1 = Poupanca(2000)
print("Conta Poupança")
print(f"Saldo atual R$ {cp1.saldo:.2f}")
cp1.sacar(100)
print(f"Saldo após saque R$ {cp1.saldo:.2f}")
cp1.depositar(100)
print(f"Saldo após depósito R$ {cp1.saldo:.2f}")