"""Peça um número de CPF digitado sem pontos nem traço (ex: 12345678900) 
e formate-o no padrão 123.456.789-00.
Dica: fatiamento e f-strings."""

while True:

    cpf = input("Digite o CPF sem pontos nem traços: ").strip()

    if len(cpf) == 11 and cpf.isdigit():

        novoCPF = cpf[0:3]+"."
        novoCPF = novoCPF+cpf[3:6]+"."
        novoCPF = novoCPF+cpf[6:9]+"-"
        novoCPF = novoCPF+cpf[9:11]

        print(novoCPF)
        break
    else:
        print("O CPF deve ter 11 dígitos e somente números!")
