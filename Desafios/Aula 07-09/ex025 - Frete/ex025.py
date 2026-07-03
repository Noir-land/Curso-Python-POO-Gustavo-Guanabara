"""
Crie classes capazes de calcular frete de veiculos diferetes

Classe:
________________________________________________________
Transporte {abstract}
________________________________________________________
+ distancia
+ frete
________________________________________________________
+ calc_frete() {abstract}
________________________________________________________

SubClasse:
_________________  _________________   _________________
Moto               |Caminhao           | Drone
_________________  |________________   |________________
+ fator = 0.5      |+ fator = 1.2      | + fator = 9.5
_________________  |________________   |________________
+ calc_frete()     |+ calc_frete()     | + calc_frete()
_________________  |________________   |_________________

frete de Moto é livre, Caminhão 50 km e Drone 10 km
"""

from abc import ABC, abstractmethod
from rich.traceback import install
from rich import print
install()


class Transporte(ABC):
    def __init__(self, dist):
        self.distancia = dist
        self.min_dista = 50
        self.max_dista = 10
        self.frete = 0

    @abstractmethod
    def calc_frete(self):
        pass


class Moto(Transporte):
    fator = 0.5
    def __init__(self, dist):
        super().__init__(dist)

    def calc_frete(self):
        self.frete = self.distancia * Moto.fator
        return f'Custará R$ [blue]{self.frete:.2f}[/]'.replace('.', ',')


class Caminhao(Transporte):
    fator = 1.2
    def __init__(self, dist):
        super().__init__(dist)

    def calc_frete(self):
        match self.distancia >= max(self.min_dista, self.max_dista):
            case True:
                self.frete = (self.distancia * self.fator) * Caminhao.fator
                return f'Custará R$ [blue]{self.frete:.2f}[/]'.replace('.', ',')
            case False:
                return f'Distância mínima  de {max(self.min_dista, self.max_dista)}Km'


class Drone(Transporte):
    fator = 9.5
    def __init__(self, dist):
        super().__init__(dist)

    def calc_frete(self):
        match self.distancia <= min(self.min_dista, self.max_dista):
            case True:
                self.frete = self.distancia * Drone.fator
                return f'Custará R$ [blue]{self.frete:.2f}[/]'.replace('.', ',')
            case False:
                return f'Distância mínima de {min(self.min_dista, self.max_dista)}Km'
