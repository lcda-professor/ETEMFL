import conexao

def listar():
    try:

        conn = conexao.conexao()
        
        cursor = conn.cursor()

        sql = "select * from alunos;"

        cursor.execute(sql)

        alunos = cursor.fetchall() #retorna vários resultados na busca (como tupla)

        for i in alunos:
            print(f"{i[0]} {i[1]}") #cada coluna da tupla pode ser acessado pelo índice

        cursor.close()
        conn.close()

    except:
        print("Erro na consulta!")