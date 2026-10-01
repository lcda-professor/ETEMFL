'''Continue com a classe Conta e adicione o seguinte:

1. Crie um método para sacar. O saque só poderá ser realizado 
se o valor não for negativo nem for menor que o saldo.
2. Crie um método para depositar. O depósito só poderá ser 
realizado se o valor não for negativo.
3. No programa principal crie um menu com as seguintes opções:
1-Sacar
2-Depositar
3-Ver saldo
0-Sair'''

class Conta:
    def __init__(self, saldo):
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, valor):
        self._saldo = valor
    
    def sacar(self, valor):
        if valor < 0:
            return("Valor não pode ser negativo!")
        elif valor > self.saldo:
            return("Valor deve ser acima do saldo!")
        else:
            self.saldo = self.saldo - valor
            return("Saque realizado!")
    
    def depositar(self, valor):
        if valor < 0:
            return("Valor não pode ser negativo!")
        else:
            self.saldo += valor
            return("Depósito realizado!")
        
#Principal

c1 = Conta(0)
while True:
    print("MENU")
    print("1-Sacar")
    print("2-Depositar")
    print("3-Ver saldo")
    print("0-Sair")
    op=int(input("Digite uma opção: "))
    match(op):
        case 1:
            while True:
                valor=float(input("Qual valor a ser sacado?(0 para sair): "))
                if valor==0:
                    break
                elif valor > 0:
                    print(c1.sacar(valor))
                    input()
                    break
                else: print("Digite um valor acima de R$ 0")
        case 2:
            while True:
                valor=float(input("Qual valor a ser depositado?(0 para sair): "))
                if valor==0:
                    break
                elif valor > 0:
                    print(c1.depositar(valor))
                    input()
                    break;
                else: print("Digite um valor acima de R$ 0")
        case 3: 
            print(c1.saldo)
            input()
        case 0:
            break
        case _:
            print("Opção inválida! Digite uma opção do menu!")
            input()
