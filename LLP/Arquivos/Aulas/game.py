import random
import os

# caminho relativo
relativo = "Arquivos/Aulas/arquivo.txt"

# converte para absoluto
caminho_absoluto = os.path.abspath(relativo)

print("Caminho absoluto:", caminho_absoluto)

acertos = 0
erros = 0

def salvar():
    with open ("arquivo.txt", "w") as arquivo:
        arquivo.write(f"{acertos}\n")
        arquivo.write(f"{erros}")

with open ("arquivo.txt", "r") as arquivo:

    if arquivo:
        l = 0
        for linha in arquivo:
            if l ==0:
                acertos = int(linha.strip())
                l+=1
            else:
                erros = int(linha.strip())
                
while True:
    os.system("clear")
    print(f"---Seus acertos: {acertos} pontos!---\n")
    print(f"---Seus erros: {erros} pontos!---\n")
    num = int(input("Digite um numero entre 1 e 5 ou qualquer outro para encerrar!"))
    
    if(-1 < num < 6):
        if num == random.randint(1,10):
            print("Você acertou!")
            acertos += 10
            #salvar()
            input()
        else:
            print("Ah, não foi dessa vez!")
            erros += 10
            input()
    else:
        salvar()
        break