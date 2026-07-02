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
        self._base = base
        self._altura = altura
        self._area = 0

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, valor):
        self._base = abs(valor)

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, valor):
        self._altura = abs(valor)

    @property
    def medidas(self):
        self.area
        return f'Base: {self._base}\nAltura: {self._altura}\nArea: {self._area}'

    @medidas.setter
    def medidas(self, valor):
        self._base = valor[0]
        self._altura = valor[1]

    @property
    def area(self):
        self._area = self._altura * self._base
        return self._area

    @area.setter
    def area(self):
        return self._area
