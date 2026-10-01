'''Faça um algoritmo que solicite duas temperaturas
e mostre a menor delas ou se são iguais. As temperaturas
deverão ser verificadas e impressas dentro de um módulo
def, passando as temperaturas como parâmetros

def temperaturas(t1, t2):
    if t1 > t2:
        print(t1," é maior")
    elif t2 > t1:
        print(t2," é maior")
    else:
        print(t1," e ",t2," são iguais")

t1 = float(input("Digite a primeira temp.: "))
t2 = float(input("Digite a segunda temp.: "))

temperaturas(t1,t2)'''






'''Uma loja deseja analisar o desempenho de vendas
realizadas durante  o dia. O programa deve solicitar
o valor de cada venda (valores reais positivos).
A entrada de dados deve ser encerrada quando o  usuário
digitar 0'''

qtd=0; soma=0; maior50=0; menor20=0; valorVenda=1

valorVenda = float(input("Digite o valor da venda: "))
if valorVenda > 0 or valorVenda != 0:
    maior=valorVenda
    menor=valorVenda

while valorVenda > 0 or valorVenda != 0:
    if valorVenda < 0:
        print("valor inválido!")
    elif valorVenda == 0:
        break
    else:
        qtd+=1
        soma+=valorVenda
        
        if valorVenda > maior:
            maior = valorVenda
        if valorVenda < menor:
            menor = valorVenda
        if valorVenda >= 50:
            maior50+=1
        if valorVenda < 20:
            menor20+=1
    
    valorVenda = float(input("Digite o valor da venda: "))

print(f"{qtd} vendas realizadas")
print(f"R${soma:.2f} em vendas realizadas")
print(f"O valor médio de vendas foi de R${soma/qtd:.2f}")
print(f"O maior valor de venda foi de R${maior:.2f}")
print(f"O menor valor de vend foi de R${menor:.2f}")
print(f"{maior50} vendas a partir de R$50,00")
print(f"{menor20} vendas menores que R$20,00")


