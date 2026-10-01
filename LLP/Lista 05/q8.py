def mensagem(maior):
    print(f"Foram digitadas {maior} idades pares")

def entradas(maior, nome):
    while nome != "sair":
        nome = input("Digite um nome: ")
        if nome != "sair":
            idade = int(input("Digite a idade: "))
            if idade > 18:
                maior+=1
    return maior

def cadastro():
    maior = 0
    nome = ""
    maior = entradas(maior,nome)
    return maior

def main():
    maior = cadastro()
    mensagem(maior)
    print("FIM")

main()

