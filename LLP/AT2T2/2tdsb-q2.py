# Dada a lista preços = [20.45, 42.95, 35.19, 13.45, 9.90], 
# escreva um programa que calcule a média dos preços da lista 
# e depois conte e imprima quantos valores estão abaixo da 
# média e quantos estão acima da média.

precos = [20.45, 42.95, 35.19, 13.45, 9.90]

media = 0
abaixo = 0
acima = 0

for p in precos:
    media+=p

media = media / 5

for p in precos:
    if p < media:
        abaixo+=1
    else:
        acima+=1

print(f"Média dos preços R$ {media:.2f}")
print(f"Quantidade de preços ABAIXO da média: {abaixo}")
print(f"Quantidade de preços ACIMA da média: {acima}")