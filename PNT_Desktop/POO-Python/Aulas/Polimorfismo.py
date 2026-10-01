class Conta:
    def __init__(self, saldo):
        self._saldo = saldo

    @property #get
    def saldo(self):
        return self._saldo
    
    @saldo.setter #set
    def saldo(self, valor):
        self._saldo = valor
    
    #método de saque padrão para as duas contas
    def sacar(self, valor):
        self.saldo-=valor
    
    #método de depósito padrão para as duas contas
    def depositar(self, valor):
        self.saldo+=valor

class Corrente(Conta):
    def __init__(self, saldo):
        super().__init__(saldo)
    
    #método sacar que sobrescreve o de Conta
    def sacar(self, valor):
        valorTarifado = valor + (valor*2.1)/100
        self.saldo -= valorTarifado

class Poupanca(Conta):
    def __init__(self, saldo):
        super().__init__(saldo)
    
    #método depositar que sobrescreve o de Conta
    def depositar(self, valor):
        valorTarifado = valor + (valor*0.5)/100
        self.saldo += valorTarifado

print("SAQUE NAS CONTAS\n")

cc1 = Corrente(1000)
print("---Conta Corrente---")
print(f"Saldo atual R$ {cc1.saldo:.2f}")
cc1.sacar(100)
print(f"Saldo após saque R$ {cc1.saldo:.2f}")

cp1 = Poupanca(1000)
print("---Conta Poupança---")
print(f"Saldo atual R$ {cp1.saldo:.2f}")
cp1.sacar(100)
print(f"Saldo após saque R$ {cp1.saldo:.2f}")

print("\nDEPÓSITO NAS CONTAS\n")

print("---Conta Corrente---")
print(f"Saldo atual R$ {cc1.saldo:.2f}")
cc1.depositar(100)
print(f"Saldo após depósito R$ {cc1.saldo:.2f}")

print("----Conta Poupança---")
print(f"Saldo atual R$ {cp1.saldo:.2f}")
cp1.depositar(100)
print(f"Saldo após depósito R$ {cp1.saldo:.2f}")