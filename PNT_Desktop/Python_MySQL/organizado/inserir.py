import mysql.connector

try:
    conexao = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="escola"
            )
    cursor = conexao.cursor()

    '''#INSERT
    valores = ("Enzo", 20, 1)

    sql = f"insert into alunos (nome, idade, id_curso) values (%s, %s, %s);"

    cursor.execute(sql, valores)

    conexao.commit() #função commit confirma a operação (inserção) dos dados o BD

    #SELECT
    sql = f"select * from alunos;"

    cursor.execute(sql)

    alunos = cursor.fetchall()

    for aluno in alunos:
        print(aluno)'''

    #UPDATE
    nome = "Enzo"
    idade = 50
    id_curso = 1
    id = 14

    valores = (nome, idade, id_curso, id)

    sql = """
        UPDATE alunos
        SET nome = %s, idade = %s, id_curso = %s
        WHERE id_aluno = %s
        """

    cursor.execute(sql, valores)

    conexao.commit()

    #SELECT
    sql = f"select * from alunos;"
    
    cursor.execute(sql)
    
    alunos = cursor.fetchall()
    
    for aluno in alunos:
        print(aluno)
    
    cursor.close()
    conexao.close()


except Exception as e:
    print(e)