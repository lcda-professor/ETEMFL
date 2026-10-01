
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
1-Inserir
2-Consultar
3-Remover
4-Alterar
0-Sair
          """)
    op = int(input("Digite a opção: "))

    match op:
        case 1: #Inserção
            pessoa["nome"] = input("Digite o nome: ")
            pessoa["idade"] = input("Digite a idade: ")
            pessoa["cpf"] = input("Digite o CPF: ")
            pessoa["email"] = input("Digite o email: ")
            while True:
                telefone = input("Digite o telefone ou sair: ")
                if telefone != "sair":
                    pessoa["telefones"].append(telefone)
                else:
                    break
            lista_pessoas.append(pessoa.copy())
        
        case 2: #Consulta
            cpf = input("Digite o CPF para consulta: ")
            encontrado = False
            for pessoa in lista_pessoas:
                if pessoa["cpf"] == cpf:
                    print("Registro encontrado!")
                    print(f"Nome: {pessoa["nome"]}")
                    print(f"E-mail: {pessoa["email"]}")
                    encontrado=True
                    input()
                    break
            
            if(encontrado == False):
                print("CPF não encontrado!")

        case 3: #Remoção
            cpf = input("Digite o CPF para consulta: ")
            encontrado = False
            for pessoa in lista_pessoas:
                if pessoa["cpf"] == cpf:
                    print("Registro encontrado!")
                    op = input(f"Deseja remover {pessoa["nome"]}? S-Sim N-Não: ")
                    if op == "S":
                        lista_pessoas.remove(pessoa)
                        print("Remoção efetuada!")
                    else:
                        print("Remoção cancelada!")
                    encontrado = True
                    input()
                    break
            
            if(encontrado == False):
                print("CPF não encontrado!")
        case 4: #Alteração
            cpf = input("Digite o CPF para consulta: ")
            encontrado = False
            for pessoa in lista_pessoas:
                if pessoa["cpf"] == cpf:
                    print("Registro encontrado!")
                    print("MENU DE ALTERAÇÃO")
                    print("""
1-Nome
2-Idade
3-CPF
4-E-mail
0-Sair""")
                    
                    op = int(input("Digite a opção de alteração: "))
                    match(op):
                        case 1:
                            print(f"Nome: {pessoa["nome"]}")
                            nome = input("Digite o novo nome: ")
                            pessoa["nome"] = nome
                            lista_pessoas[lista_pessoas.index(pessoa)] = pessoa
                            print("Nome alterado!")
                        case 0:
                            break
                        case _: print("Opção inválida!")
                    encontrado=True
                    input()
                    break
            
            if(encontrado == False):
                print("CPF não encontrado!")
        case 0:
            break
        case _:
            print("opção invalida!")

