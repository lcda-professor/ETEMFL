"""3. Peça ao usuário uma palavra e verifique se ela é um palíndromo 
(ou seja, se é igual quando lida ao contrário). Ignore maiúsculas e espaços.
Exemplo:
→ “Ame a ema” → é palíndromo.
Dica: use replace(" ", ""), lower(), [::-1]."""

palavra = input("Digite uma palavra: ").strip().lower()
palavra = palavra.replace(" ","")
invertida = palavra[::-1]

if palavra == invertida:
    print(f"{palavra} é um palíndromo.")
else:
    print(f"{palavra} não é um palíndromo.")