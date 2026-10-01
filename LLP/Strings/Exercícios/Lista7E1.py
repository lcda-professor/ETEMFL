while True:

    nome = input("Digite o seu nome completo: ").strip()

    ultimoNome = len(nome.split())


    if ultimoNome > 1:
        print(f"Primeiro nome com letra maiúscula: {nome.split()[0].title()}")
        print(f"Último nome com letra maiúscula: {nome.split()[ultimoNome-1].title()}")
        print(f"O seu nome tem {len(nome.replace(" ",""))} caracteres sem espaços")
        break
    else:
        print("Digite pelo menos um sobrenome")
