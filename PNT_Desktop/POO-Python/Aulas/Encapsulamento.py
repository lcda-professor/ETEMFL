class Conta:
    def __init__(self, saldo):
        self._saldo = saldo

    @property #get
    def saldo(self):
        return(self._saldo)
    
    @saldo.setter #set
    def saldo(self, valor):
        self._saldo+=valor

c1 = Conta(50)
print(f"Saldo inicial: R${c1.saldo}")
c1.saldo = 100
print(f"Novo saldo: {c1.saldo}")








    #get -> ler o atributo
    def saldo_get(self):
        return self._saldo

    #set -> escrever o atributo
    def saldo_set(self, valor):
        self._saldo += valor

c1 = Conta(50)

print(f"Saldo inicial: R${c1.saldo_get()}")
c1.saldo_set(100)
print(f"Novo saldo: {c1.saldo_get()}")