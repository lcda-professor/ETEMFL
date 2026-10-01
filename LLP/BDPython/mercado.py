import mysql.connector
import os

def limparTela(msg):
    print(msg)
    input()
    os.system("clear")


#Conexão com o banco
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root@1234",
    database="teste"
)

limparTela("Conexão realizada com sucesso!")

cursor = conn.cursor()

while True:
    print("""---MENU---
1 - Clientes
2 - Produtos
3 - Vendas
0 - Sair""")
    op = int(input("Digite a opção: "))

    match op:
        case 1:
            os.system("clear")
            print("""---MENU DE CLIENTE---
1 - Cadastrar cliente
2 - Remover cliente
3 - Alterar cliente
4 - Consultar cliente
0 - Voltar""")
            op = int(input("Digite a opção: "))

            match(op):
                case 1:
                    os.system("clear")
                    print("---CADASTRO DE CLIENTE")
                    nome = input("Nome do cliente: ")
                    cpf = input("CPF do cliente: ")
                    nasc = input("Data de nascimento: ")
                    
                    conf = input("Confirmar cadastro? S-sim N-Não: ")

                    if conf != "n":
                        sql = "insert into cliente (nome, nasc, cpf) values (%s, %s, %s)"
                        valores = (nome, nasc, cpf)
                        cursor.execute(sql, valores)

                        try:
                            conn.commit()
                            print("Cliente cadastrado!")
                        except:
                            print("O cliente não foi cadastrado.")
                        limparTela("")
                case 0:
                    break
        case 0:
            break