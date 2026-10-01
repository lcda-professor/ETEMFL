# Dada a lista valores = [2, 4, 6, 8, 10], escreva um programa que multiplique 
# cada elemento pelo seu índice na lista.

valores = [2, 4, 6, 8, 10]

indice = 0
soma = 0

for i in valores:
    print(f"{indice} x {i} = {indice*i}")
    indice+=1