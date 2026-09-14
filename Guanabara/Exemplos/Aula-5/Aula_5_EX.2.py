class ContaBancaria:
    '''
    Cria uma conta bancaria e permite saques e depósitos
    '''

    def __init__(self, id, titular, saldo=0):
        self.id = id
        self.titular = titular
        self.saldo = saldo
        print(f'Conta {self.id} criada com sucesso. Saldo atual R${self.saldo:,.2f}')

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
            print('Saque NEGADO de R${valor:,.2f} na conta {self.id}: SALDO INSUFICIENTE')


print('')
c1 = ContaBancaria(122 ,'Thaison', 1000)
c1.depositar(40000)
c1.sacar(12000)
print(c1)
print('')





'''c1 = ContaBancaria(112, 'Thaison', 850)
opcao = 1
while opcao != 0:
    print('='*20)
    print('1 - Depositar')
    print('2 - Sacar')
    print('3 - Ver Saldo')
    print('0 - Sair Menu')
    print('='*20)
    opcao = int(input('Escolha: '))
    match opcao:
        case 1:
            c1.depositar(int(input('Digite um valor: ')))
        case 2:
            c1.sacar(int(input('Digite um valor: ')))
        case 3:
            print(c1)'''