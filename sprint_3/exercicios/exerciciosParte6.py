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

#--------------------------------------------------------------------------------------------------------------------------------------#

"""
E22 - Crie uma classe chamada Pessoa, com um atributo privado chamado nome (declarado internamente na classe como __nome) e um atributo público de nome id.
      Adicione dois métodos à classe, sendo um para definir o valor de __nome e outro para retornar o valor do respectivo atributo.
      
      Lembre-se que o acesso ao atributo privado deve ocorrer somente através dos métodos definidos, nunca diretamente.  Você pode alcançar este comportamento através do recurso de properties do Python.
      
      Veja um exemplo de como seu atributo privado pode ser lido e escrito:
      
      pessoa = Pessoa(0)
      pessoa.nome = 'Fulano De Tal'
      print(pessoa.nome)
"""

class Pessoa:
    
    __nome = ''
    id = ''

    def __init__(self, id):
        self.id = id


    @property
    def nome (self):
        return self.__nome
    

    @nome.setter
    def nome (self, nome):
        self.__nome = nome


p = Pessoa(0)
p.nome = ("Fulano de Tal")
print(p.nome)
    