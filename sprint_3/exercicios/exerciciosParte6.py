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
    
#--------------------------------------------------------------------------------------------------------------------------------------#

"""
E23 - Crie uma classe  Calculo  que contenha um método que aceita dois parâmetros, X e Y, e retorne a soma dos dois. 
      Nessa mesma classe, implemente um método de subtração, que aceita dois parâmetros, X e Y, e retorne a subtração dos dois 
      (resultados negativos são permitidos).

      Utilize os valores abaixo para testar seu exercício:

      x = 4 
      y = 5
      imprima:

      Somando: 4+5 = 9
      Subtraindo: 4-5 = -1
"""

class Calculo:

    def soma(x, y):
        soma = x+y
        print("Somando: {}+{} = {}".format(x, y, soma))
    
    def sub (x, y):
        sub = x-y
        print("Subtraindo: {}-{} = {}".format(x, y, sub))
    
Calculo.soma(4, 5)
Calculo.sub(4, 5)

#--------------------------------------------------------------------------------------------------------------------------------------#

"""
E24 - Crie uma classe Ordenadora que contenha um atributo listaBaguncada e que contenha os métodos ordenacaoCrescente e ordenacaoDecrescente.
      Instancie um objeto chamado crescente dessa classe Ordenadora que tenha como listaBaguncada a lista [3,4,2,1,5] e instancie um outro objeto,
      decrescente dessa mesma classe com uma outra listaBaguncada sendo [9,7,6,8].

      Para o primeiro objeto citado, use o método ordenacaoCrescente e para o segundo objeto, use o método ordenacaoDecrescente.

      Imprima o resultado da ordenação crescente e da ordenação decresce

      [1, 2, 3, 4, 5] 
      [9, 8, 7, 6]
"""

class Ordenadora:

    def __init__(self, lista):
        self.listaBaguncada = lista


    def ordenacaoCrescente(self):
        listaC = sorted(self.listaBaguncada)
        return listaC


    def ordenacaoDecrescente(self):
        listaD = sorted(self.listaBaguncada)
        return listaD[::-1]


crescente = Ordenadora([3,4,2,1,5])
print(crescente.ordenacaoCrescente())

decrescente = Ordenadora([9,7,6,8])
print(decrescente.ordenacaoDecrescente())
