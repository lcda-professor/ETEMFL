class Tarefa:
    def __init__(self, nome):
        self.__nome = nome
        self.__tempo = 0

    @property
    def nome(self):
        return self.__nome

    @property
    def tempo(self):
        return self.__tempo
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @tempo.setter
    def tempo(self, tempo):
        self.__tempo = tempo

    def calcular_tempo(self):
        return self.__tempo

class TarefaComplexa(Tarefa):
    def calcular_tempo(self):
        return self.tempo * 2

class TarefaSimples(Tarefa):
    def calcular_tempo(self):
        return self.tempo / 2

#Principal

#Objetos
tarefa_simples = TarefaSimples("Organizar arquivos")
tarefa_complexa = TarefaComplexa("Desenvolver sistema")

tarefa_simples.tempo = 4
tarefa_complexa.tempo = 4

print("Tarefa Simples:")
print(f"Nome: {tarefa_simples.nome}")
print("Tempo Estimado:", tarefa_simples.tempo)
print("Tempo Real:", tarefa_simples.calcular_tempo())

print("\nTarefa Complexa:")
print("Nome:", tarefa_complexa.nome)
print("Tempo Estimado:", tarefa_complexa.tempo)
print("Tempo Real:", tarefa_complexa.calcular_tempo())