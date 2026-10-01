def calcular_media(lista):
    media = 0
    for i in lista:
        media = media + i
    media = media/len(lista)

    return media

#principal
notas = []
idades = []

while True:
    nota = float(input("Digite a nota ou -1 para sair: "))
    if nota == -1:
        break
    else:
        notas.append(nota)

while True:
    idade = int(input("Digite a idade ou -1 para sair: "))
    if idade == -1:
        break
    else:
        idades.append(idade)

print(f"A media das notas é {calcular_media(notas)}")
print(f"A media das idades é {calcular_media(idades)}")

