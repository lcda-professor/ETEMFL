class Corrida:
   def __init__(self, distancia, tempo):
       self._distancia = distancia
       self._tempo = tempo
  
   @property
   def distancia(self):
       return self._distancia
  
   @property
   def tempo(self):
       return self._tempo
  
   @distancia.setter
   def distancia(self, valor):
       self._distancia = valor
  
   @tempo.setter
   def tempo(self, valor):
       self._tempo = valor


   def mostrar_preco(self):
       preco = 3 + (1.7*self.distancia) + (0.3*self.tempo)
       return preco
  
class Economica(Corrida):
   def __init__(self, distancia, tempo):
       super().__init__(distancia, tempo)
  
   def mostrar_preco(self):
       preco = 2 + (1.2*self.distancia) + (0.2*self.tempo)
       return preco


class Normal(Corrida):
   def __init__(self, distancia, tempo):
       super().__init__(distancia, tempo)


class Premium(Corrida):
   def __init__(self, distancia, tempo):
       super().__init__(distancia, tempo)
  
   def mostrar_preco(self):
       preco = 5 + (2.5*self.distancia) + (0.5*self.tempo)
       return preco


#Principal


while True:
   distancia = float(input("Digite a distância percorrida em Km: "))
   tempo = int(input("Digite o tempo da corrida em minutos: "))


   print("1-Economica\n" \
   "2-Normal\n" \
   "3-Premium\n" \
   "0-Sair")
   op = int(input("Digite a opção: "))


   match(op):
       case 1:
           e1 = Economica(distancia, tempo)
           print(f"O valor da corrida Econômica foi R$ {e1.mostrar_preco():.2f}")
       case 2:
           n1 = Normal(distancia, tempo)
           print(f"O valor da corrida Normal foi R$ {n1.mostrar_preco():.2f}")
       case 3:
           p1 = Premium(distancia, tempo)
           print(f"O valor da corrida Premium foi R$ {p1.mostrar_preco():.2f}")
       case 0:
           break
       case _:
           print("Opção inválida!")

