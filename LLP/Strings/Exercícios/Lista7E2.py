frase = input("Digite uma frase: ").strip()
fraseLetras = frase.replace(" ","").lower()

vogais = set("aeiouáàâãäéèêëíìîïóòôõöúùûüýÿ")
qtdVogais = 0
qtdConsoantes = 0

for letra in fraseLetras:
    if letra.isalpha():
        if letra in vogais:
            qtdVogais+=1
        else:
            qtdConsoantes+=1

print(f"Quantidade de vogais: {qtdVogais}")
print(f"Quantidade de consoantes: {qtdConsoantes}")