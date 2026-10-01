# Dada a lista valores = [3, 8, 5, 1, 9, 2, 7, 4], escreva um algoritmo 
# que calcule e imprima a soma dos elementos que estão nas posições pares 
# da lista.

valores = [3, 8, 5, 1, 9, 2, 7, 4]

posicao=1
soma = 0

for i in valores:
    if posicao%2==0:
        soma = soma+i
    posicao+=1
print(f"A soma dos valores pares é {soma}")