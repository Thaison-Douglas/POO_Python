class ContaBancaria:
    banco = 'Banco Tung Tung'                   # atributo de CLASSE (comum a todos)
    total_contas = 0                            # contador compartilhado

    def __init__(self, titular, saldo=0):
        self.titular = titular                  # atributo de INSTANCIA (individual)
        self.saldo = saldo
        ContaBancaria.total_contas += 1

    def ver_saldo(self):
        print(f'[{self.banco}] {self.titular}: R$ {self.saldo:.2f}')

c1 = ContaBancaria('Bombardiro Crocodilo', 100)
c2 = ContaBancaria('Ballerina Cappuccina', 200)
c1.ver_saldo()
c2.ver_saldo()
print('Contas criadas:', ContaBancaria.total_contas)