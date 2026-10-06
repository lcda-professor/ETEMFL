import conexao

def consultar_por_id(id):
    try:
        conn = conexao.conexao()

        cursor = conn.cursor()

        sql = "select * from alunos where id_aluno = %s;" #uso de placeholder - marcador de parâmetro para consulta parametrizada

        cursor.execute(sql, (id,)) #neste caso o execute exige passagem de dois parâmetros: a querry completa e o valor do parâmetro como tupla

        aluno = cursor.fetchone() #retorna um resultado na busca

        return(aluno) #Pode retornar os dados do aluno (tupla) ou None se não achar
    except Exception as e:
        print(e)
        return False