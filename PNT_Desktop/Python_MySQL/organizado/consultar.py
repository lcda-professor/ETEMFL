import conexao

def consultar_por_id(id):
    try:
        conn = conexao.conexao()

        cursor = conn.cursor()

        sql = "select * from alunos where id_aluno = %s;"

        cursor.execute(sql, (id,))

        aluno = cursor.fetchone()

        return(aluno) #Pode retornar os dados do aluno (tupla) ou None se não achar
    except Exception as e:
        print(e)
        return False