"""Peça que o usuário crie uma senha e verifique se ela é forte.
Critérios:
· Mínimo de 8 caracteres
· Contém pelo menos 1 letra maiúscula
· 1 letra minúscula
· 1 número
· 1 caractere especial (!@#$%&*)
Mostre mensagens específicas indicando o que falta.
Dica: any(), isupper(), islower(), isdigit()."""

senha = input("""Digite o senha de usuario contendo ao menos 8 caracteres, contendo pelo menos:
· 1 letra maiúscula
· 1 letra minúscula
· 1 número
· 1 caractere especial (!@#$%&*)
Digite: """)

if (any(c.isalpha() for c in senha)):
    if(any(c.isupper() for c in senha)):
        if(any(c.islower() for c in senha)):
            if(any(c.isdigit() for c in senha)):
                if(any(not c.isalnum() for c in senha)):
                    print("Senha válida! Deve conter pelo menos 8 caracteres.")
                else:
                    print("Deve conter algum caractere especial!")
            else:
                print("Deve conter algum número!")
        else:
            print("Deve ter pelo menos uma letra minúscula!")
    else:
        print("Deve ter pelo menos uma letra maiúscula!")
else:
    print("Deve conter uma letra!")

