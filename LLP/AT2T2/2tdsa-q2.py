# Dada a lista temperaturas = [22.5, 20.0, 23.1, 26.7], escreva um programa 
# que calcule a média dos valores da lista e depois conte e imprima quantos 
# valores estão acima da média.

temperaturas = [22.5, 20.0, 23.1, 26.7]

media = 0
acima = 0

for temp in temperaturas:
    media+=temp
media = media/4

for temp in temperaturas:
    if temp > media:
        acima+=1
print(f"Média das temperaturas: {media}")
print(f"Quantidade de temperaturas acima da média: {acima}")
