"""
Implemente um 'termostato' orientado a objetos.
minimo 16ºc 
máximo 30ºc
inicia 24ºc
incremento 0.5ºc

Classe:
__________________
Termostato
__________________
- __temperatura
@property
+ @temperatura 
+ @ftemperatura
__________________


"""

from rich import print, inspect


class Termostato:
    def __init__(self, valor=24):
        self.__temperatura = valor

    @property
    def temperatura(self):  # getter
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, valor):  # setter
        if 16 <= valor <= 30:
            verific = valor + valor
            if verific % 1 == 0:
                self.__temperatura = valor
            else:
                print(
                    f'A temperatura {valor}ºc é invalida. Ajustando temperatura para {round(valor)}ºc')
                self.__temperatura = round(valor)
        else:
            if 16 > valor:
                self.__temperatura = 16
            elif 30 < valor:
                self.__temperatura = 30

    @property
    def ftemperatura(self):
        return f'{self.temperatura}ºc'
