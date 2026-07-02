'''
Aprimore o exercicio(Aula 5 e 10) da Contabancária, aplicando conceitos de encapsulamento

Classe 
_________________________
ContaBancaria:
_________________________
# _id
# _titular
- __saldo
- __hash
+ @nome
_________________________
+ validar_senha(chave)
+ pede_senha()
+ sacar(valor, chave)
+ depositar(valor)
_________________________
'''
from getpass import getpass
from rich import print, inspect


class ContaBancaria:
    def __init__(self, id, titular, saldo, chave=None):
        self._id = id
        self._titular = titular
        self.__saldo = saldo
        self.__hash = hash(chave)
        self.pede_senha()

    @property
    def nome(self):
        return self._titular

    @nome.setter
    def nome(self, msg):
        if self.validar_senha() == True:
            print(f'Nome alterado com sucesso. Novo nome: {msg}')
            self._titular = msg

    def validar_senha(self, chave: str = None) -> bool:
        if chave is None:
            chave = hash(getpass('Digite a senha de verificação ', echo_char='*'))
            if self.__hash == chave:
                print('Validação bem sucedida.')
                return True
            else:
                print('Erro na validação')
                return False
        else:
            chave = hash(chave)
            if self.__hash == chave:
                print('Validação bem sucedida.')
                return True
            else:
                print('Erro na validação.')
                return False

    def pede_senha(self):
        if self.__hash is None:
            self.__hash = hash(
                getpass('Digite a senha: ', echo_char='*'))
            print(f'Conta {self._id} criada com sucesso. Seu saldo é de R${self.__saldo:,.2f}.')

    def sacar(self, valor: float = 0, chave=None):
        valor = abs(valor)
        if chave is None:
            chave = hash(getpass('Digite a senha de verificação de saque: ', echo_char='*'))
            print('Senha correta')
            print(f'Saque liberado. Valor sacado R${valor:,.2f} na conta {self._id}.')
        else:
            if self.validar_senha(chave) == True:
                self.__saldo -= valor
                print('Senha correta')
                print(f'Saque liberado. Valor sacado R${valor:,.2f} na conta {self._id}.')
            else:
                print('Senha incorreta.')

    def depositar(self, valor):
        valor = abs(valor)
        self.__saldo += valor
        print(f'Deposito efetuado com sucesso. Valor depositado R${valor:,.2f} na conta {self._id}.')
