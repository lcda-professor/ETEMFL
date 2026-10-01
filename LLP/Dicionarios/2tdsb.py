import os

pessoa = {
    "nome": None,
    "idade": 0,
    "email": None,
    "cpf": None
}

pessoas = []

while True:
    print("1-Inserir")
    print("2-Excluir")
    print("3-Alterar")
    print("4-Consultar")
    print("5-Listar")
    print("0-Sair")
    op = int(input("Digite a opção: "))

    match op:
        case 1:
            pessoa["nome"] = input("Digite o nome: ")
            pessoa["idade"] = int(input("Digite a idade: "))
            pessoa["email"] = input("Digite o e-mail: ")
            pessoa["cpf"] = input("Digite o CPF - só números: ")
            pessoas.append(pessoa.copy())
            print("Registro realizado!")
            input()
            os.system("clear")

        case 2:
            cpf = input("Digite o CPF - só números: ")
            encontrado = False
            if len(pessoas) > 0:
                for i in pessoas:
                    if cpf == i["cpf"]:
                        pessoas.pop(pessoas.index(i))
                        print("Remoção efetuada!")
                        input()
                        os.system("clear")
                        encontrado = True
                        break
                if not encontrado:
                    print("CPF não cadastrado!")
                    input()
                    os.system("clear")
            else:
                print("Não há registros!")
                input()
                os.system("clear")
        
        case 3:
            cpf = input("Digite o CPF - só números: ")
            encontrado = False
            if len(pessoas) > 0:
                for i in pessoas:
                    if cpf in i["cpf"]:
                        print("""
---MENU DE ALTERAÇÃO---
1-Nome
2-CPF
3-Idade
4-E-mail
0-Sair
                              """)
                        op = int(input("O que você deseja alterar? "))
                        match op:
                            case 1:
                                i["nome"] = input("Digite o novo nome: ")
                                pessoas[pessoas.index(i)] = i
                                print("Nome alterado!")
                                input()
                                os.system("clear")
                            case 2:
                                i["cpf"] = input("Digite o novo CPF: ")
                                pessoas[pessoas.index(i)] = i
                                print("CPF alterado!")
                                input()
                                os.system("clear")
                            case 3:
                                i["idade"] = input("Digite a nova idade: ")
                                pessoas[pessoas.index(i)] = i
                                print("Idade alterada!")
                                input()
                                os.system("clear")
                            case 4:
                                i["email"] = input("Digite a nova idade: ")
                                pessoas[pessoas.index(i)] = i
                                print("E-mail alterado!")
                                input()
                                os.system("clear")
                            case 0:
                                break
                            case _:
                                print("opção inválida!")
                                input()
                                os.system("clear")
                        
                        encontrado = True
                if not encontrado:
                    print("CPF não cadastrado!")
                    input()
                    os.system("clear")
            else:
                print("Não há registros!")
                input()
                os.system("clear")

        case 4:
            cpf = input("Digite o CPF - só números: ")
            encontrado = False
            if len(pessoas) > 0:
                for i in pessoas:
                    if cpf in i["cpf"]:
                        print("Registro encontrado!")

                        print(f"Nome: {i["nome"]}")
                        print(f"Idade: {i["idade"]}")
                        print(f"E-mail: {i["email"]}")
                        print(f"CPF: {i["cpf"]}")
                        
                        input()
                        os.system("clear")
                        encontrado = True
                        break
                if not encontrado:
                    print("CPF não cadastrado!")
                    input()
                    os.system("clear")
            else:
                print("Não há registros!")
                input()
                os.system("clear")
        case 5:
            if len(pessoas) > 0:
                for i in pessoas:
                    print(f"Nome: {i["nome"]}")
                    print(f"Idade: {i["idade"]}")
                    print(f"E-mail: {i["email"]}")
                    print(f"CPF: {i["cpf"]}")
                    print("----------------------")
            else:
                print("Não há registros!")
                input()
                os.system("clear")

            input()
            os.system("clear")

        case 0:
            print("Encerrando... aperte Enter para sair.")
            input()
            os.system("clear")
            break
        case _:
            print("Opção inválida!")