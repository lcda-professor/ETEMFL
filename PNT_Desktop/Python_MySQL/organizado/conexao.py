import mysql.connector

def conexao():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="escola"
        )
        print("Ok")
        return conexao

    except mysql.connector.errors.ProgrammingError:
        print("Erro de usuário ou senha.")

conexao()


