import os
def verSaldo(saldo):
    print(f"Saldo atual R$: {saldo}")

def depositar(saldo, valor):
    saldo = saldo + valor
    return saldo
    
def sacar(saldo, valor):
    if saldo >= valor:
        saldo = saldo - valor
        msg = "Saque realizado!"
    else:
        msg = "Saldo insuficiente!"
    
    return saldo, msg

def menu():
    saldo = 0
    while True:
        input()
        os.system("clear")
        print("""
1-Sacar
2-Depositar
3-Saldo
0-Sair""")
        op = int(input("Digite a opção: "))
        match op:
            case 1:
                valor = float(input("Digite o valor a sacar: "))
                saldo, msg = sacar(saldo, valor)
                print(msg)
                verSaldo(saldo)
            
            case 2:
                valor = float(input("Digite o valor a depositar: "))
                saldo = depositar(saldo, valor)
                print("Depósito efetuado!")
                verSaldo(saldo)

            case 3:
                verSaldo(saldo)

            case 0:
                break

            case _:
                print("Opção inválida!")

#principal
menu()