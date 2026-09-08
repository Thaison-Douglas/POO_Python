class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def ver_saldo(self):
        print(f'{self.titular}: R$ {self.saldo:.2f}')


class ContaPoupanca(ContaBancaria):           # herda de ContaBancaria
    def render_juros(self, taxa):
        self.saldo += self.saldo * taxa

poupanca = ContaPoupanca("Thaison", 1000)
poupanca.render_juros(0.10)
poupanca.ver_saldo()