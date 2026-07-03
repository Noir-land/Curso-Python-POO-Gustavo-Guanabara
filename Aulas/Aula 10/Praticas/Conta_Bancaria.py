class ContaBancaria:
    """
Cria uma conta bancária e permite a retirada e reposidos
    """

    def __init__(self, id, nome, saldo=0):
        self.id = id
        self._titular = nome
        self.__saldo = saldo
        print(  f'Conta {self.id} foi criada com sucesso. __Saldo atual de R$ {self.__saldo:,.2f}')

    def __str__(self):
        return f'A conta {self.id} de {self._titular} tem R$ {self.__saldo:,.2f} de saldo.'

    def deposito(self, valor):
        valor = abs(valor)
        self.__saldo += valor
        print(
            f'Deposito de R$ {valor:,.2f}. Foi autorizado na conta {self.id}.')

    def sacar(self, valor):
        valor = abs(valor)
        if valor <= self.__saldo and self.__saldo > 0:
            self.__saldo -= valor
            print(f'Saque de R$ {valor:,.2f}. Foi autorizado na conta {self.id}.')
        else:
            print(f'Saque de R$ {valor:,.2f}. Não foi autorizado.')


