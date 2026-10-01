#Questão 1
def nomeCompleto():
    while True:
        nome = input("Digite o seu nome completo: ").strip()
        nomeFat = nome.split()
        if len(nomeFat) > 1:
            nomeSobrenome = nomeFat[0]+" "+nomeFat[-1]
            break
        else:
            print("Digite pelo menos um sobrenome.")
    return nomeSobrenome.title()

#Questão 2
def dataNascimento():
    global data
    while True:
        data = input("Informa a data de nascimento no formato DD/MM/AAAA: ").strip()
        if data.replace("/","").isdigit():
            if data[0:2].isdigit() and data[2] == "/" and data[3:5].isdigit and data[5] == "/" and (data[6:10].isdigit() and len(data[6:10]) == 4):
                return(data)
            else:
                print("Data tem que ser no formato DD/MM/AAAA")
        else:
            print("Data só deve conter números!")

#Questão 3
def senhaAcesso():
    while True:
        senha = input("""Digite um senha forte
                    no mínimo 8 números, 2 caracteres especiais 
                    e que nao contenha a data de nascimento
                    : """).strip()

        d = 0 #Contador de dígitos
        e = 0 #Contador de caracteres especiais
        for c in senha:
            if c.isdigit():
                d+=1
            if not c.isalnum():
                e+=1
        
        if d >= 8: #Se tiver pelo menos 8 números
            if e >= 2: #Se tiver pelo menos 2 caracteres especiais

                #Verifica ao mesmo tempo se a data de nascimento está na senha
                #tanto apenas os dígitos quanto com a barra /
                if not senha.find(data) or senha.find(data.replace("/","")):
                    return "*" * len(senha)
                else:
                    print("Não pode conter a data de nascimento")
            else:
                print("Deve conter pelo menos dois caracteres especiais")
        else:
            print("Deve conter pelo menos 8 números")

#Questão 4
def telefoneFormatado():

    listaDDDs = [11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 24, 27, 28, 31, 32, 33, 34, 35, 37, 38, 41, 42, 43, 44, 45, 46, 47, 48, 49, 51, 53, 54, 55, 61, 62, 63, 64, 65, 66, 67, 68, 69, 71, 73, 74, 75, 77, 79, 81, 82, 83, 84, 85, 86, 87, 88, 89, 91, 92, 93, 94, 95, 96, 97, 98, 99]

    while True:
        tel = input("Digite o telefone com DDD e os nove dígitos, somente números: ").strip()

        if len(tel) == 11:
            if int(tel[0:2]) in listaDDDs:
                tel = f"({tel[0:2]}) {tel[2]}.{tel[3:7]}-{tel[7:11]}"
                return tel
            else:
                print("Digite um DDD válido.")
        else:
            print("O telefone precisa ter 11 dígitos (incluindo DDD).")

#Questão 5
def emailValido():

    dominios = [".com", ".com.br", ".org", ".org.br"]

    while True:
        email = input("Digite o seu e-mail com domínio terminado em .com, .com.br, .org ou .org.br: ").strip()

        #Aqui poderia ser usado if "@" in email, porém como um endereço de e-mail
        #só aceita um @, é preciso verificar isso com a condicional abaixo
        if email.count("@") == 1:
            
            #Separar o endereço em duas partes: nome de usuário e domínio
            emailSemArroba = email.split("@")

            if len(emailSemArroba[0]) >= 3: #Verifica se o nome de usuário tem pelo menos 3 caracteres
                dominio = emailSemArroba[1].split(".") #Separa o domínio em duas partes: antes e depois da terminação
                if len(dominio[0]) >= 3: #Verifica se o domínio possui pelo menos 3 caracteres antes da terminação
                    if emailSemArroba[1].find(".com" or ".com.br" or ".org" or ".org.br"): #Verifica o término do domínio
                        return email
                    else:
                        print("O domínio precisa terminar com .com, .com.br, .org ou .org.br")
                else:
                    print("O domínio precisa ter pelo menos 3 caracteres mais a terminação válida.")             
            else:
                print("O nome de usuário precisa ter pelo menos 3 caracteres.")
        else:
            print("O endereço deve ter um '@'. Exemplo: ana@cac.com")

def mensagemFinal():
    nome = nomeCompleto()
    data = dataNascimento()
    senha = senhaAcesso()
    telefone = telefoneFormatado()
    email = emailValido()

    print("-------------------------------------------------------")
    print("")
    print("CADASTRO CONFIRMADO")
    print(f"Nome: {nome}")
    print(f"Data de Nascimento: {data}")
    print(f"Senha: {senha}")
    print(f"Telefone: {telefone}")
    print(f"E-mail: {email}")
    print("-------------------------------------------------------")


#Início do programa
mensagemFinal()