while True:
    cpf = input("Digite o CPF (apenas dígitos): ")
    if len(cpf) == 11:
        print("CPF OK!")
        break;
    else:
        print("CPF inválido. Deve ter 11 dígitos.")
