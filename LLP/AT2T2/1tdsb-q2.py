# Dada a lista pecas = [10, 22, 19, 14, 18, 15, 11, 13], 
# onde cada número representa o total de peças produzidas 
# em dias consecutivos de trabalho, escreva um programa 
# que calcule e imprima a soma da produção somente dos 
# dias pares.

pecas = [10, 22, 19, 14, 18, 15, 11, 13]
dia = 1
soma = 0

for i in range(1,8,2):
    soma+=i

for quantidade in pecas:
    if dia%2 == 0:
        soma+=quantidade
    dia+=1

print(f"Total de peças produzidas nos dias pares foi: {soma}")