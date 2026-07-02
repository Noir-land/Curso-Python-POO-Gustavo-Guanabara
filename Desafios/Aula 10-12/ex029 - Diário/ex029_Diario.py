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


class Diario:
    def __init__(self, senha=1234):
        self.__segredos = list()
        self.__senha = senha

    def escrever(self, msg):
        return self.__segredos.append(msg)

    def ler(self, msg=0):
        if msg == self.__senha:
            print('Senha aceita.')
            for i in self.__segredos:
                print(f'- {i}')
        else:
            print('senha invalida')
