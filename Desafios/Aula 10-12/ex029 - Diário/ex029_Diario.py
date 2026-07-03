'''
Simule um diário secreto orientado a objetos

Classe
_____________________
Diario
_____________________
- __segredos list[]
- __senha
_____________________
+ escrever(msg)
+ ler(senha)
_____________________
'''
from getpass import getpass

class Diario:
    def __init__(self, senha='1234'):
        self.__segredos = list()
        self.__senha = senha

    def escrever(self, msg):
        return self.__segredos.append(msg)

    def ler(self, msg=None):
        if msg is None:
            msg = getpass('Digite a senha: ', echo_char='*').strip()
        if str(msg) == self.__senha:
            print('Senha aceita.')
            for i in self.__segredos:
                print(f'- {i}')
        else:
            raise PermissionError('Senha invalida!')

    def senha(self, msg=''):
        senha = getpass('Digite a senha atual: ', echo_char='*').strip()
        if senha == self.__senha:
            self.__senha = getpass('Digite a nova senha: ',echo_char='*').strip()