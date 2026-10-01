class Animal:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, idade):
        self._idade = idade
    
    def fazerSom(self):
        return "O animal faz som!"
    
class Cachorro(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
    
    def fazerSom(self):
        return "Au Au"

class Gato(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
    
    def fazerSom(self):
        return "Miau"

c1 = Cachorro("Pluto", 5)
g1 = Gato("Tom", 7)

print(c1.nome)
print(c1.idade)
print(c1.fazerSom())

print(g1.nome)
print(g1.idade)
print(g1.fazerSom())
