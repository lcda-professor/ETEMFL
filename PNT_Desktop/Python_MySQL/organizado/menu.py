import inserir, consultar as back_consulta, listar

def menu_inserir():
    nome = input("Digite o nome do estudante: ")
    idade = int(input("Digite a idade do estudante: "))
    id_curso = int(input("Digite o id do curso 1-TDS 2-MKT"))

    valores = (nome, idade, id_curso)

    return valores

def consultar():

    id = int(input("Informa o ID do aluno: "))
    
    aluno = back_consulta.consultar_por_id(id)

    resultado = None

    if aluno != None:
        if aluno != False:
            id, nome, idade, id_curso = aluno
            resultado = f"ID: {id}\n Nome: {nome}\n Idade: {idade}\n Curso: {id_curso}"
        else:
            resultado = "Erro ao consultar!"
    else:
        resultado = "Nenhum aluno encontrado com este ID."

    return resultado
def menu():
    op = -1

    while op!= 0:
        print("---MENU---\n")
        print("1 - Inserir")
        print("4 - Consultar")
        print("5 - Listar")
        print("0 - Sair")
        op = int(input("Digite a opção: "))

        match op:
            case 1:
                if inserir.inserir(menu_inserir()):
                    print("Aluno registrado!")
                else:
                    print("Erro ao registrar o estudante!")
            case 4:
                    print(consultar())
            case 5:
                listar.listar()
            case 0:
                print("Sistema encerrado!")
            case _: print("Opção inválida!")