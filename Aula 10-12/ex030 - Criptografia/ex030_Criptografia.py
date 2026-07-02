'''
Crie uma classe que gerencie a 'hash SHA256' de uma senha

Classe
___________________ 
Credencial
___________________ 
+ @senha
- __hash
___________________ 
+ validar(chave)
___________________ 
'''
from rich import print, inspect


class Credencial:
    def __init__(self, senha=''):
        self.senha = senha
        self.__hash = senha

    @property
    def senha(self):
        return self.__hash

    @senha.setter
    def senha(self, chave):
        self.__hash = hash(chave)
        return self.__hash

    def validar(self, chave) -> bool:
        if hash(chave) == self.__hash:
            print('Acesso permitido')
            return True
        else:
            print('Acesso negado')
            return False
