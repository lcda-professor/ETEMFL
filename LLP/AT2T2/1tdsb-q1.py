# Dada a lista idades = [12, 17, 19, 15, 23, 14, 18, 21, 13], 
# escreva um programa que imprima primeiro as idades dos 
# menores de idade e a quantidade total deles e em seguida 
# imprima as idades dos maiores de idade e a quantidade total 
# deles, sabendo que a maioridade é a partir dos 18 anos.

idades = [12, 17, 19, 15, 23, 14, 18, 21, 13]
menor = 0
maior = 0

for i in idades:
    if i < 18:
        print(i)
        menor+=1
print(f"Quantidade de menores de idade: {menor}")

for i in idades:
    if i >= 18:
        print(i)
        maior+=1
print(f"Quantidade de maiores de idade: {maior}")