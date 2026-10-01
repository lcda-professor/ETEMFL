# Dada a lista valores = [3, 8, -5, 1, 9, -2, 7, -4], 
# escreva um algoritmo que calcule e imprima primeiro 
# os números negativos e a quantidade total deles e 
# depois imprima os números positivos e a quantidade 
# total deles.

valores = [3, 8, -5, 1, 9, -2, 7, -4]

negativos = 0
positivos = 0

for v in valores:
    if v < 0:
        print(v)
        negativos+=1
print(f"Total de números negativos: {negativos}")

for v in valores:
    if v > 0:
        print(v)
        positivos+=1
print(f"Total de números positivos: {positivos}")