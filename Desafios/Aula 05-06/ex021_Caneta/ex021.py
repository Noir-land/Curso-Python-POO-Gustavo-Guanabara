"""
Crie a classe Caneta, que simule o funcionamento de uma caneta colorida
pdendo escrever frases na cor relativa
"""
from rich.traceback import install
from rich import print
install()


class Caneta:
    def __init__(self, cor=''):
        self.cor = cor
        self.destampada = False
        self.cores = {'verde': 'green', 'vermelho': 'red'}

    def destampar(self):
        self.destampada = True

    def tampar(self):
        self.destampada = False

    def escrever(self, msg=''):
        if self.cor in self.cores:
            if self.destampada:
                print(f'[{self.cores[self.cor]}]{msg}[/]')
            else:
                print(
                    f'A [{self.cores[self.cor]}]caneta[/] não esta destampada.')
        else:
            print('Não existe a cor')

    def quebar_linha(self, qnt=1):
        print("\n" * qnt, end='')


p1 = Caneta('verde')
p2 = Caneta('vermelho')

p2.destampar()
p1.tampar()

p1.escrever('olá')
p1.quebar_linha(2)
p2.escrever('Eu sei')
