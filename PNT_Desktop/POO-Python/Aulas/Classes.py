
class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.idade = None
    
    def imprimirDados(self):
        print(f"Nome: {self.nome}")
        print(f"idade: {self.idade}")


# codigo principal
p1 = Pessoa("João")
print(p1.nome)
p1.idade = 25

p2 = Pessoa("Marta")
print(p2.nome)
p2.idade = 62

p1.imprimirDados()
p2.imprimirDados()