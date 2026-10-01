class Animal:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade
    
    def fazerSom(self):
        return "Faz um som!"

class Gato(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
    
    #def fazerSom(self):
    #    return "miau!"

class Cachorro(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
    
    def fazerSom(self):
        return "Au au!"

g1 = Gato("Mikael", 90)
c1 = Cachorro("Guenzo", 15)

print(g1.fazerSom())
print(c1.fazerSom())