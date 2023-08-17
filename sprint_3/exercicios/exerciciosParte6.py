#--------------------------------------------------------------------------------------------------------------------------------------#
 # Seção 6: Exercícios Python || - 1/2
#--------------------------------------------------------------------------------------------------------------------------------------#


"""
E21 - implemente duas classes Pato e Pardal que herdem de uma classe Passaro a habilidade de voar e emitir som, porém, tanto Pato quanto Pardal devem emitir sons diferentes (de maneira escrita) no console.
      Imprima no console exatamente assim:

      Pato
      Voando...
      Pato emitindo som...
      Quack Quack
      Pardal
      Voando...
      Pardal emitindo som...
      Piu Piu
"""

class Passaro:

    def __init__(self, especie):
        self.voar = True
        self.especie = especie
        print('{}'.format(self.especie))
        print('Voando...')
    
    def som(self, som):
        self.som = som
        print("{} emitindo som...".format(self.especie))
        print("{}".format(self.som))


class Pato(Passaro):

    def __init__(self, especie):
        super().__init__(especie)
    
    def som(self, som):
        Passaro.som(self, som)


class Pardal(Passaro):

    def __init__(self, especie):
        super().__init__(especie)
    
    def som(self, som):
        Passaro.som(self, som)


obj1 = Pato('Pato')
obj1.som('Quack Quack')

obj2 = Pardal('Pardal')
obj2.som('Piu Piu')