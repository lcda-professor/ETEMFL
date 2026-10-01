from collections import namedtuple
from tqdm import tqdm
import os, pickle, time

registro = []

# 🔹 pega o diretório onde este script .py está
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 🔹 monta o caminho absoluto para a pasta Cadastro/dados
arquivo_nome = "registro.dat"
caminho = os.path.join(BASE_DIR, "Cadastro", "dados", arquivo_nome)

# 🔹 garante que a pasta existe
os.makedirs(os.path.dirname(caminho), exist_ok=True)

if not os.path.exists(caminho):
    with open(caminho, "wb") as arquivo:  # usa modo binário
        pickle.dump([], arquivo)  # salva lista vazia

Pessoa = namedtuple("Pessoa",["id","nome","idade","cpf","tel"])
id = 0

def salvarArquivo():
    print("Salvando registros...")
    with open(caminho, "wb") as arquivo:
        pickle.dump(registro, arquivo)
    for _ in tqdm(range(100)):
        time.sleep(0.02)  # simula processamento
    print("\nRegistro salvo com sucesso!")
    input()
    os.system("clear")

def carregarArquivo():
    print("Carregando registros...")
    try:
        with open(caminho, "rb") as arquivo:
            dados = pickle.load(arquivo)
    except (EOFError, FileNotFoundError):
        dados = []  # se vazio, retorna lista vazia
    for _ in tqdm(range(100)):
        time.sleep(0.02)  # simula processamento
    print("\nRegistro carregado com sucesso!")
    input()
    os.system("clear")
    return(dados)

registro = carregarArquivo()

while True:
    print("""
    1-Cadastrar
    2-Excluir
    3-Alterar
    4-Consultar
    5-Listar
    6-Salvar
    7-Carregar Registros
    0-Sair""")

    op = int(input("Digite a opção: "))
    os.system("clear")

    match op:
        case 1:
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            cpf = input("CPF (apenas números): ")
            tel = input("Telefone (apenas números): ")

            os.system("clear")

            print(f"""
            Nome: {nome}
            Idade: {idade}
            CPF: {cpf}
            Tel: {tel}""")
            op=""

            while op.lower!="s" and op.lower!="n":
                op = input("Confirma os dados? S-Sim / N-Não: ")
                if op.lower()=="s":
                    id+=1
                    p = Pessoa(id,nome,idade,cpf,tel)
                    registro.append(p)
                    os.system("clear")
                    print("Registro realizado!")
                    break
                elif op.lower()=="n":
                    os.system("clear")
                    print("Operação cancelada!")
                    break
                else:
                    os.system("clear")
                    print("Opção inválida!")     

        case 2:
            id = int(input("Digite o ID para remoção: "))

            for p in registro:
                if id == p.id:
                    i = registro.index(p)
                    op = input(f"Deseja mesmo remover {p.nome}? S-Sim / N-Não: ")
                    if op.lower()=="s":
                        registro.pop(i)
                        os.system("clear")
                        print("Exclusão efetuada!")
                        break
                    elif op.lower()=="n":
                        print("Operação cancelada!")
                        break
                    else:
                        print("Opção inválida!")
                        os.system("clear")
                        break
                if(registro.index(p) == len(registro)-1):
                    print("Nenhum registro encontrado!")

        case 3:
            print("A fazer...")

        case 4:
            while True:
                print("""
                    1-Por ID
                    2-Por CPF
                    0-Sair""")
                op = int(input("Escolha o tipo de consulta: "))
                os.system("clear")
                match op:
                    case 1:
                        print("a fazer...")
                    case 2:
                        cpf = input("Digite o CPF: ")
                        for p in registro:
                            if cpf == p.cpf:
                                print(f"""
                                        ID: {p.id}
                                        Nome: {p.nome}
                                        Idade: {p.idade}
                                        CPF: {p.cpf}
                                        Tel: {p.tel}""")
                                break
                            if(registro.index(p) == len(registro)-1):
                                print("Nenhum registro encontrado!")
                    case 0: break
                    case _: print("opção inválida!")

        case 5:
            print("-----------------")
            if len(registro)!=0:
                for p in registro:
                    print(f"""
                    ID: {p.id}
                    Nome: {p.nome}
                    Idade: {p.idade}
                    CPF: {p.cpf}
                    Tel: {p.tel}""")

                    print("-----------------")
            else:
                print("Nenhum registro encontrado!")
                input()
                os.system("clear")
        
        case 6:
            if len(registro) == 0:
                print("Nenhum registro encontrado!")
            else:
                salvarArquivo()
            
        case 7:
            registro = carregarArquivo()
            ultimoId = len(registro)
            id = ultimoId-1
        
        case 0:
            os.system("clear")
            if len(registro) != 0:
                op = input("Deseja salvar os dados? S-Sim / N-Não: ")
                if op.lower()=="s":
                    salvarArquivo()
                elif op.lower()=="n":
                    print("Ok!")
                else:
                    print("Opção inválida!")
                break

            input("Aperte Enter para finalizar...")
            break

