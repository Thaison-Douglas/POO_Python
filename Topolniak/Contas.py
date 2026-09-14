class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente!")

    def ver_saldo(self):
        print(f'{self.titular}: R$ {self.saldo:.2f}')

conta = ContaBancaria("Bombardiro Crocodilo", 100)
conta.depositar(50)
conta.sacar(30)
conta.ver_saldo()

contas = []
for i in range(3):
    nome = input('Nome: ')
    saldo = int(input('Saldo: '))
    conta = ContaBancaria(nome, saldo)
    contas.append(conta)