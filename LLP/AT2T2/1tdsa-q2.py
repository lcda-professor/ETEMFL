# Dada a lista numeros = [15, 8, 22, 5, 19, 31, 3], escreva um programa que 
# encontre o maior e o menor valor da lista e imprima esses dois valores ao final.

numeros = [15, 8, 22, 5, 19, 31, 3]

maior = 0
menor = 32

for i in numeros:
    if i > maior:
        maior = i
    if i < menor:
        menor = i
print(f"O maior número é {maior}")
print(f"O menor número é {menor}")