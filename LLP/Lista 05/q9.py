'''Crie um programa com a seguinte lista: [2,5,6,9,11].
O programa deve exibir um menu interativo e para cada opção 
abaixo usar o match-case. O menu deve ter as seguintes opções:
1 – Somar os elementos da lista
2 - Multiplicar os elementos da lista
3 – Mostrar os números pares da lista
4 – Mostrar os números ímpares da lista
0 - Sair'''

lista = [2,5,6,9,11]

opcao = -1

while opcao != 0:
    print("""
1 – Somar os elementos da lista
2 - Multiplicar os elementos da lista
3 – Mostrar os números pares da lista
4 – Mostrar os números ímpares da lista
0 - Sair""")
    opcao=int(input("Digite a opção: "))

    match opcao:
        case 1:
            soma = 0
            for i in lista:
                soma+=i   
            print(f"A soma dos valores da lista é {soma}")
            break 
        case 2:
            mult = 1
            for i in lista:
                mult = mult*i    
                print(mult)
            print(f"A multipplicação dos valores da lista é {mult}")
        case 3:
            for i in lista:
                if i%2 == 0:
                    print(i)
        case 4:
            for i in lista:
                if i%2 !=0:
                    print(i)
        case 0:
            print("Saindo do sistema...")
            break
        case _:
            print("opção inválida!")
print("--FIM---")

