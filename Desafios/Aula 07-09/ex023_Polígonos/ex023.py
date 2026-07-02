"""
Implemente o seguinte 'diagrama de classes:

Classe
__________________________________________
Poligono {abstract}
__________________________________________
+ qnt_lados
__________________________________________
+ perimetro() {abstract}
+ area() {abstract}
__________________________________________

Subclass
________________        __________________
Quadrado                | Circulo         
________________        |_________________
+ lado                  | + raio 
________________        |_________________
+ perimetro()           | + perimetro()      
+ area()                | + area()
________________        |_________________
"""

from abc import ABC, abstractmethod
from rich import print
from rich.traceback import install
import math
install()


class Poligono(ABC):
    def __init__(self, lados):
        self.qnt_lados = lados

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Quadrado(Poligono):
    def __init__(self, lados):
        super().__init__(lados)

    def perimetro(self) -> float:
        self.calculo_peri = self.qnt_lados * 4
        return float(self.calculo_peri)

    def area(self) -> float:
        self.calculo_area = self.qnt_lados * self.qnt_lados
        return float(self.calculo_area)


class Circulo(Poligono):
    def __init__(self, raio):
        super().__init__(raio)
        self.raio = raio

    def perimetro(self):
        self.calculo_peri = (math.pi * self.qnt_lados) * 2
        return float(self.calculo_peri)

    def area(self):
        self.calculo_area = math.pi * (self.raio ** 2)
        return self.calculo_area


