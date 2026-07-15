'''
Crie uma classe que represente um retângulo pelas suas medidas e área

Classe
____________________
REtangulo
____________________
# _base
# _altura
# _area
+ @base
+ @altura 
+ @medias 
+ @area 
____________________
____________________
'''
from rich import inspect, print


class Retangulo:
    def __init__(self, base=0, altura=0):
        self._base = None
        self._altura = None
        self._area = None

        self.base = base
        self.altura = altura

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, valor):
        # self._base = abs(valor)
        if not isinstance(valor, float) and not isinstance(valor, int):
            raise TypeError('O valor de base deve ser um número')
        if valor > 0:
            raise ValueError('Valor inválido para a base')
        else:
            self._base = valor

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, valor):
        # self._altura = abs(valor)
        if not isinstance(valor, float) and not isinstance(valor, int):
            raise TypeError('O valor de base deve ser um número')
        if valor > 0:
            raise ValueError('Valor inválido para a altura')
        else:
            self._altura = valor

    @property
    def medidas(self):
        self.area
        return f'Base: {self._base}\nAltura: {self._altura}\nArea: {self._area}'

    @medidas.setter
    def medidas(self, valor: tuple):
        if not isinstance(valor, tuple):
            raise TypeError(
                'As medidas devem ser informadas dentro de uma tupla')
        if len(valor) != 2:
            raise SyntaxError(
                'Informe uma tupla com apenas dois valores numéricos')
        if isinstance(valor[0], float) or isinstance(valor[0], int):
            self.base = valor[0]
        else:
            raise TypeError('A base deve ser um número')
        if isinstance(valor[1], float) or isinstance(valor[1], int):
            self.altura = valor[1]
        else:
            raise TypeError('A altura deve ser um número')

    @property
    def area(self):
        self._area = self._altura * self._base
        return self._area

    @area.setter
    def area(self):
        return self._area
