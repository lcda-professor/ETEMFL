import conexao

def inserir(valores):
    try:
        conn = conexao.conexao()
        cursor = conn.cursor()

        sql = f"insert into alunos (nome, idade, id_curso) values (%s, %s, %s);"

        cursor.execute(sql, valores)

        conn.commit() #função commit confirma a operação (inserção) dos dados o BD
    
        cursor.close()
        conn.close()

        return True
    except:
        return False

