from rich import print

class Funcionario:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo


    def apresentacao(self):
        return f':handshake: Olá, sou [blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa Curso em Vídeo'


c1 = Funcionario('Toponiak', 'TI', 'Programador')
print(c1.apresentacao())

c2 = Funcionario('Guanabara', 'TI', 'Admintração')
print(c2.apresentacao())
