def saudacao(nome):
    return f"Olá, {nome}"

def verificar_maioridade(idade):
    if idade >= 18:
        return "Você é de maior"
    else:
        return "Você é de menor"

def exibir_informacoes(nome, idade):
    print(saudacao(nome))
    print(verificar_maioridade(idade))

#principal
nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
exibir_informacoes(nome, idade)
print("FIM")
