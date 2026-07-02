'''
Crie a classe Produto, onde podemos castrar 'nome' e o 'preço'. 
Crie também um método que mostre uma 'etiqueta' de preço do produto.
'''
from rich.panel import Panel
from rich.console import Console
from rich.traceback import install

install()
console = Console()


class Produto:
    def __init__(self, nome='', valor=0):
        self.produto = nome
        self.preco = valor

    def etiqueta(self):
        item = f'{self.produto.center(30, ' ')}'
        item += f'{"-" * 30}'
        precof = f'R${self.preco:,.2f}'
        item += f'{precof.center(30, '-')}'
        self.temp = Panel(item, title='PRODUTOS', width=34)

        return console.print(self.temp)


p1 = Produto(nome='NoteBook', valor=800)
p2 = Produto(nome='mouse', valor=120)

p1.etiqueta()
p2.etiqueta()
