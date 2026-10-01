import mysql.connector

try:
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root", #use a sua senha
        database="escola"
    )

    cursor = conexao.cursor() #primeiro cria o cursor (serve para executar comandos sql no python)
    
    sql = "select * from alunos;" # segundo cria o comando em sql
    
    cursor.execute(sql) # terceiro executa o comando sql
    
    alunos = cursor.fetchall() # quarto armazenar o resultado do BD (tuplas) em uma variável

    for i in alunos:
        print(i)

    cursor.close()
    conexao.close()
except:
    print("Erro ao conectar.")