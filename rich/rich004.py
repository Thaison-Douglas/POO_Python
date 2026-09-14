from rich import print
from rich import inspect

#inspect(int, all=True)


class ContaBancaria:
    '''
    Cria uma conta bancaria e permite saques e depósitos
    '''

    def __init__(self, id, titular, saldo=0):
        self.id = id
        self.titular = titular
        self.saldo = saldo
        print(
            f'Conta {self.id} criada com sucesso. Saldo atual R${self.saldo:,.2f}')

    def __str__(self):
        return f'A conta {self.id} de {self.titular} tem R${self.saldo:,.2f} de saldo'

    def depositar(self, valor):
        self.saldo += valor
        print(f'Deposito de R${valor:,.2f} autorizado na conta {self.id}')

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque de R${valor:,.2f} autorizado na conta {self.id}')
        else:
            print(
                'Saque NEGADO de R${valor:,.2f} na conta {self.id}: SALDO INSUFICIENTE')


c = ContaBancaria(11, 'Thaison', 1000)
inspect(c)