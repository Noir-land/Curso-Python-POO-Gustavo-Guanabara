class ContaBancaria:
    """
Cria uma conta bancária e permite a retirada e reposidos
    """

    def __init__(self, id, nome, saldo=0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(  f'Conta {self.id} foi criada com sucesso. Saldo atual de R$ {self.saldo:,.2f}')

    def __str__(self):
        return f'A conta {self.id} de {self.titular} tem R$ {self.saldo:,.2f} de saldo.'

    def deposito(self, valor):
        self.saldo += valor
        print(
            f'Deposito de R$ {valor:,.2f}. Foi autorizado na conta {self.id}.')

    def sacar(self, valor):
        if valor <= self.saldo and self.saldo > 0:
            self.saldo -= valor
            print(f'Saque de R$ {valor:,.2f}. Foi autorizado na conta {self.id}.')
        else:
            print(f'Saque de R$ {valor:,.2f}. Não foi autorizado.')


pesssoa1 = ContaBancaria(id=112, nome='Hélio', saldo=3000)
pesssoa1.deposito(500)
pesssoa1.sacar(4000)
print(pesssoa1)
