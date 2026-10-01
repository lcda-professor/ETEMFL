import conexao

def listar():
    try:

        conn = conexao.conexao()
        
        cursor = conn.cursor()

        sql = "select * from alunos;"

        cursor.execute(sql)

        alunos = cursor.fetchall()

        for i in alunos:
            print(f"{i[0]} {i[1]}") #cada coluna da tupla pode ser acessada pelo índice

        cursor.close()
        conn.close()

    except:
        print("Erro na consulta!")