import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="escola")


cursor = conexao.cursor()

nome = "Maria Silva"
idade = 18
id_curso = 2

sql = 'INSERT INTO aluno (nome, idade, id_curso) VALUES (%s, %s, %s);'

dados = (nome, idade, id_curso)

cursor.execute(sql, dados)
conexao.commit()

#commit
#fetchall

cursor.close()
conexao.close()
print("ok")