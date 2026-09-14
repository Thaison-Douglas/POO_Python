class Aluno:

    def __init__(self, nome, idade, curso, nota):
        self.nome = nome
        self.idade = idade
        self.curso = curso
        self.nota = nota

    def mostrar_dados(self):
        print(f'Nome: {self.nome} | Idade: {self.idade} | Curso: {self.curso} | Nota: {self.nota}.')

    def alterar_nota(self, nota):
        self.nota = nota

    def situacao(self):
        if self.nota >= 60:
            print(f'Aluno {self.nome} do curso de {self.curso} está APROVADO!')
        else:
            print(f'Aluno {self.nome} do curso de {self.curso} está REPROVADO!')


a1 = Aluno('Thaison', 15, 'TI', 50)
a1.mostrar_dados()
a1.situacao()
a1.alterar_nota(nota=int(input(f'Digite a nova NOTA do aluno: ')))
a1.mostrar_dados()
a1.situacao()