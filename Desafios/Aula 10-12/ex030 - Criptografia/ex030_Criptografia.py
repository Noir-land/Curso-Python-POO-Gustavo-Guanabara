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
from hashlib import sha256
from getpass import getpass
from rich.traceback import install
install()


class Credencial:
    def __init__(self):
        self.__hash = None

    @property
    def senha(self):
        return self.__hash

    @senha.setter
    def senha(self, chave: str):
        if chave == '':
            chave = getpass('Defina uma senha: ', echo_char='*')
            if len(chave) < 8:
                print('A senha deve ter no minímo 8 caracteres.')
                return
            else:
                chave = sha256(chave.encode('utf-8')).hexdigest()
                self.__hash = chave
                return self.__hash

        self.__hash = sha256(chave.encode('utf-8')).hexdigest()
        return self.__hash

    def validar(self, chave: str) -> bool:
        if sha256(chave.encode('utf-8')).hexdigest() == self.__hash:
            print('Acesso permitido')
            return True
        else:
            print('Acesso negado')
            return False
