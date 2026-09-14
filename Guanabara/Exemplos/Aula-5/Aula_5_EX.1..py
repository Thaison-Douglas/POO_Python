# Declaração de Classe
class Gafanhoto:
    '''
    Essa classe cria um Gafanhoto, que é uma pessoa que tem nome e idade

    Para criar uma nova pessoa, use
    variavel = Gafanhoto(nome, idade)
    '''

    def __init__(self, nome='vazio', idade=0):  # Método Contrutor
        # Atributos de Instância
        self.nome = nome
        self.idade = idade

    # Métodos de Instância
    def aniversario(self):
        self.idade += 1

    def __str__(self): # DUNDER METHOD
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade'

    def __getstate__(self):
        return f'Estado: nome = {self.nome} ; idade = {self.idade}'


print('')
# Declaração de Objetos
g1 = Gafanhoto('Maria', 17)
g1.aniversario()
print(g1)
print(g1.__getstate__()) # METHOD
print(g1.__class__) # Dunder Attribute


#print(g1.__dict__) # Dunder ATTRIBUTE

#print(g1.mensagem())
#print(g1.__doc__) # DUNDER ATTRIBUTE

print('')