import os

# registro de pessoas
lista_pessoas = []

# Dicionário pessoa
pessoa = {
    "nome": None, 
    "idade": None, 
    "cpf": None, 
    "telefones": [], 
    "email": None
}

while True:
    print("""
---MENU---
          
1-Inserir
2-Consultar
0-Sair
          """)
    op = int(input("Digite a opção: "))

    match op:
        case 1:
            os.system("clear")
            # Inserção de dados em Pessoa
            pessoa["nome"] = input("Digite o nome: ")
            pessoa["idade"] = int(input("Digite a idade: "))
            pessoa["cpf"] = input("Digite o CPF: ")
            pessoa["email"] = input("Digite o e-mail: ")
            while True:
                telefone = input("Digite o telefone ou sair: ")
                if telefone != "sair":
                    pessoa["telefones"].append(telefone)
                else:
                    break

            # Inserção da Pessoa na Lista de Pessoas
            lista_pessoas.append(pessoa.copy())
            print("Cadastro realizado!")
            input()
        
        case 2:
            cpf = input("Digite o CPF a ser pesquisado: ")

            encontrado = False
            for p in lista_pessoas:
                if cpf == p["cpf"]:
                    print("Regostro encontrado!")
                    print(f"Nome: {p["cpf"]}")
                    print(f"Idade: {p["idade"]}")
                    print(f"E-mail: {p["email"]}")
                    for i in p["telefones"]:
                        print(f"Telefone: {i}")
                    encontrado = True
                    input()
                    break
            
            if encontrado == False:
                print("CPF não cadastrado!")
                input()
        
        case 0:
            print("Encerrando...")
            input()
            break

        case _:
            print("Opção inválida!")

