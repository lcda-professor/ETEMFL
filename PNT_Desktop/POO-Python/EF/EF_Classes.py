'''Escreva um algoritmo com uma classe: Casa.
-Toda casa tem um numero, um bairro e um municipio.
-Todo objeto casa deve inicializar seus atributos.
-A classe casa tem um método que verifica se a casa está em Caruaru 
e retorna uma das mensagens: "Pertence ao município" 
ou "Não pertence ao município".
-Crie dois objetos de casa. Modifique o bairro de um objeto e o número de outro objeto.
-Verifique se as casas pertencem ao município de Caruaru
-Imprima todos os dados das duas casas.'''

class Casa:
    def __init__(self, numero, bairro, cidade):
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
    
    def verificarCidade(self):
        if self.cidade == "Caruaru":
            return "Pertence ao município."
        else:
            return "Não pertence ao município."
    
    def imprimirDados(self):
        return f"Número: {self.numero} - Bairro: {self.bairro} - Cidade: {self.cidade}"
    


#Principal (front-end)

c1 = Casa(12,"Salgado","Caruaru")
c2 = Casa(134,"São José","Agrestina")

c1.bairro = "José Liberato"
c2.numero = 13

print(f"Casa 1: {c1.verificarCidade()}")
print(f"Casa 2: {c2.verificarCidade()}")
print(f"Dados de Casa 1: {c1.imprimirDados()}")
print(f"Dados da Casa 2: {c2.imprimirDados()}")


