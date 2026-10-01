lista = []

while True: 
    x = input("Digite o nome de uma fruta ou sair para encerrar: ")

    if x != "sair":
        lista.append(x)

        for i in lista:
            print(i)
    else:
        break