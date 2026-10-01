frutas = []

while True:
    print("""
    ---MENU---
    1-Inserir
    2-Excluir
    3-Listar
    4-Limpar
    5-Alterar
    0-Sair""")
    op = int(input("Escolha uma das opções: "))

    match op:
        case 1:
            fruta = input("Digite o nome da fruta: ")
            frutas.append(fruta)
            print("Fruta inserida com sucesso!")
        case 2:
            print("""
1-Remover por nome da fruta
2-Remover a última fruta
0-Desistir""")
            op = int(input("Digite a opção: "))

            match op:
                case 1:
                    if len(frutas) != 0:
                        fruta = input("Digite o nome da fruta a remover: ")
                        if fruta in frutas:
                            frutas.remove(fruta)
                            print("Fruta deletada!")
                        else:
                            print(f"A fruta {fruta} não está na lista.")
                    else:
                        print("Lista vazia!")
                case 2:
                    if len(frutas) != 0:
                        frutas.pop()
                        print("A ultima fruta da lista foi excluida com sucesso")
                    else:
                        print("lista vazia!")
        case 3:
            c=1
            for f in frutas:
                print(f"{c}-{f}")
                c+=1
        case 4:
            frutas.clear();
            print("A lista foi limpa!")
        
        case 5:
            fruta = input("Qual fruta você quer alterar? ")
            if fruta in frutas:
                indice = frutas.index(fruta)
                novo_nome = input("Digite o novo nome: ")
                frutas[indice] = novo_nome
                print("O nome foi alterado!")
            else:
                print(f"{fruta} não está na lista!")
                    
        case 0:
            break
        case _:
            print("opção inválida")