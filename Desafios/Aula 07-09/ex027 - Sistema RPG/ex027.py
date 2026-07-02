"""
Simule o sistema de 'batalha' entre personagens de um RPG

Classe 
___________________________
Personagem {abstract}
___________________________
+ nome
+ vida
+ golpes
___________________________
+ atacar (alvo, forca)
+ receber_dano(dano)
+ curar() {abstract}
___________________________

SubClasse
___________     ___________
Guerreiro       |Mago
___________     |__________
+ curar()       |+ curar()
___________     |__________

"""

from abc import ABC, abstractmethod
from random import randint
from rich import print


class Personagem(ABC):
    def __init__(self, nome, vida):
        super().__init__()
        self.nome = nome
        self.vida_max = vida
        self.vivo = True

    def atacar(self, alvo, forca):
        self.alvo = alvo
        if self.alvo.__dict__['vivo']:
            self.forca = forca
            self.dano = randint(0, self.forca)
            self.atk = self.golpes[randint(0, len(self.golpes)-1)]
            return self.receber_dano(self.dano)
        else:
            print('O adversario já esta morto')

    def receber_dano(self, dano):
        if self.vivo:
            self.dano = dano
            print(
                f'Nome: [bright_magenta]{self.nome}[/] \nClasse: {self.__class__.__name__} \nHP: {self.vida_max}/{self.vida} \nAtacou [purple]{self.alvo.__dict__['nome']}[/],'
                f'com um [blue]{self.atk}[/] de força: {self.forca}\n[purple]{self.alvo.__dict__['nome']}[/] recebeu [red]dano de {self.dano} pontos![/]')

            self.alvo.__dict__['vida_max'] = self.alvo.__dict__[
                'vida_max'] - self.dano

            if self.alvo.__dict__['vida_max'] > 0:
                print(
                    f'[purple]{self.alvo.__dict__['nome']}[/] HP {self.alvo.__dict__['vida_max']}/{self.alvo.__dict__['vida']}\n')
            else:
                self.alvo.__dict__['vivo'] = False
                print(f'[purple]{self.alvo.__dict__['nome']}[/] Morreu!\n')

    @abstractmethod
    def curar():
        pass


class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['Espada', 'Soco']
        self.vida = self.vida_max

    def curar(self):
        if self.vivo:
            if self.vida_max >= 1:
                self.cura = randint(1, 500)
                print(
                    f'[purple]{self.nome}[/] usou uma poção de cura, e se [green]curou em {self.cura} pontos[/]')
                print(
                    f'[purple]{self.nome}[/] HP {self.cura+self.vida_max}/{self.vida}\n')
        else:
            print('[yellow]Impossivel Curar[/]')


class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['Bola de fogo', 'Seta de raio']
        self.vida = self.vida_max

    def curar(self):
        if self.vivo:
            if self.vida_max >= 1:
                self.cura = randint(1, 500)
                print(
                    f'[purple]{self.nome}[/] usou magia de cura, e se [green]curou em {self.cura} pontos[/]')
                print(
                    f'[purple]{self.nome}[/] HP {self.cura+self.vida_max}/{self.vida}\n')
        else:
            print('[yellow]Impossivel Curar[/]')
