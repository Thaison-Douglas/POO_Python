class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.nome = titular
        self.saldo = saldo

    def ver_saldo(self):
        print(self.saldo)

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            return 'Saldo insuficiente'

class ContaPoupanca(ContaBancaria):
    def render_juros(self, taxa):
        self.saldo += self.saldo * taxa


opcao = 1
while opcao != 0:
    print('='*20)
    print('1 - inserir conta')
    print('2 - ver saldo')
    print('3 - depositar')
    print('4 - sacar')
    print('5 - render juros')
    print('0 - Sair do menu')
    print('='*20)
    opcao = int(input('Escolha uma opção: '))
    print('='*20)
    match opcao:
        case 1:
            g1 = ContaPoupanca(input('Escreva o nome do titular: '), int(input('Digite o saldo inicial da sua conta: ')))
        case 2:
            g1.ver_saldo()
        case 3:
            g1.depositar(int(input('Digite o valor que quer depositar: ')))
        case 4:
            g1.sacar(int(input('Digite o valor que quer sacar: ')))
        case 5:
            g1.render_juros(int(input('Insira o valor da taxa: ')))