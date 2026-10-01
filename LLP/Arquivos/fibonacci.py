numero = int(input("Digite quantas vezes voce deseja a sequencia: "))

a=0
b=1

for i in range(numero):
   soma = b+a
   print(f"{b}+{a}={soma}")
   a = b
   b = soma