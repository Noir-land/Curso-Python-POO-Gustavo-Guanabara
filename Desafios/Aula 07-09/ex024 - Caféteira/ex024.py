'''
Simule uma 'cafeteira' orentada a objetos

Classe:
________________________________________________________________
BebidaQuente {abstract}
________________________________________________________________
+ preparar()
+ fever_agua()
+ misturar() {abstract}
+ servir() {abstract}
________________________________________________________________

SubClasse:
______________          ______________           _______________
Cafe                    |Cha                     |Leite
______________          |_____________           |______________
______________          |_____________           |______________
+ misturar()            |+ misturar()            |+ misturar()
+ servir()              |+ servir()              |+ servir()
______________          |______________          |______________
'''
from abc import ABC, abstractmethod


class BebidaQuente(ABC):
    def preparar(self):
        print(' Iniciando o preparo '.center(50, '-'))
        return self.fever_agua(), self.misturar(), self.servir()

    def fever_agua(self):
        print('Fervendo água a 100 graus Celsius')

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass


class Cafe(BebidaQuente):
    def __init__(self):
        super().__init__()

    def misturar(self):
        print('Passando a água pressurizada pelo pó de café moido')

    def servir(self):
        print('Servindo o café e uma xicara')
        print(' A bebida esta pronta '.center(50, '-'))


class leite(BebidaQuente):
    def __init__(self):
        super().__init__()

    def misturar(self):
        print('Passando a água pressurizada pelo pó de café moido, e misturando ao leite')

    def servir(self):
        print('Servindo o leite com café em uma xicara')
        print(' A bebida esta pronta '.center(50, '-'))


class Cha(BebidaQuente):
    def __init__(self):
        super().__init__()

    def misturar(self):
        print('Mergulhando as folhas de chá na água quente.')

    def servir(self):
        print('Servindo o chá e uma xicara')
        print(' A bebida esta pronta '.center(50, '-'))

