#código exemplo da aula para trabalhar CRUD com dicionário e lista

import os

def modConsulta(cpf):
            encontrado = False
            for pessoa in lista_pessoas:
                if pessoa["cpf"] == cpf:
                    encontrado=True
                    break
            
            if(encontrado == False):
                return encontrado

            return encontrado
def consultar():
            cpf = input("Digite o CPF para consulta: ")
            encontrado = modConsulta(cpf)
            
            if encontrado:
                    print("Registro encontrado!")
                    print(f"Nome: {pessoa["nome"]}")
                    print(f"E-mail: {pessoa["email"]}")
                    encontrado=True
                    input()
            
            else:
                print("CPF não encontrado!")
                input()

def inserir():
            cpf = input("Digite o CPF: ")
            encontrado = modConsulta(cpf)
            if encontrado:
                 print("CPF já existe")
            
            else:
                nova_pessoa = {
                    "cpf": cpf,
                    "nome": input("Digite o nome: "),
                    "idade": input("Digite a idade: "),
                    "email": input("Digite o email: "),
                    "telefones": []
                }

                while True:
                    telefone = input("Digite o telefone ou sair: ")
                    if telefone != "sair":
                        nova_pessoa["telefones"].append(telefone)
                    else:
                        break

                lista_pessoas.append(nova_pessoa)
                print("Cadastro realizado!")
                input()

def remover():
            cpf = input("Digite o CPF para consulta: ")
            encontrado = modConsulta(cpf)
            if encontrado:
                    print("Registro encontrado!")
                    op = input(f"Deseja remover {pessoa["nome"]}? S-Sim N-Não: ")
                    if op == "S":
                        lista_pessoas.remove(pessoa)
                        print("Remoção efetuada!")
                    else:
                        print("Remoção cancelada!")
                    encontrado = True
                    input()
            
            else:
                print("CPF não encontrado!")
                input()

def alterar():
            os.system("clear")
            cpf = input("Digite o CPF para consulta: ")
            encontrado = modConsulta(cpf)
            if encontrado:
                    print("Registro encontrado!")
                    print("MENU DE ALTERAÇÃO")
                    print("""
1-Nome
2-Idade
3-CPF
4-E-mail
0-Sair""")
                    
                    op = int(input("Digite a opção de alteração: "))
                    match op:
                        case 1:
                            print(f"Nome: {pessoa["nome"]}")
                            nome = input("Digite o novo nome: ")
                            pessoa["nome"] = nome
                            indice = lista_pessoas.index(pessoa)
                            lista_pessoas[indice] = pessoa
                            print("Nome alterado!")
                        
                        case _: print("Opção inválida!")
                    encontrado=True
                    input()
            else:
                print("CPF não encontrado!")
                input()    

def listar():
    if lista_pessoas:

                dados = {
                    "NOME" : [],
                    "IDADE" : [],
                    "CPF" : [],
                    "E-MAIL" : []
                }

                for pessoa in lista_pessoas:
                    dados["NOME"].append(pessoa["nome"])
                    dados["IDADE"].append(pessoa["idade"])
                    dados["CPF"].append(pessoa["cpf"])
                    dados["E-MAIL"].append(pessoa["email"])
                
                os.system("clear")
                input()

    else:
                print("Não há registros!")
                input()

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
    os.system("clear")
    print("""
1-Inserir
2-Consultar
3-Remover
4-Alterar
5-Listar
0-Sair
          """)
    op = int(input("Digite a opção: "))

    match op:
        case 1: inserir()
            
        case 2: consultar()
            
        case 3: remover()
            
        case 4: alterar()
            
        case 5: listar()

        case 0:
            break
        case _:
            print("opção invalida!")
            input()