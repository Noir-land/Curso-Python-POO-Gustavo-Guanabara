'''
Crie a classe Churasco, onde seja possivel informar
'quantas pessoas' vão participar e mostre 'quantao de carne' deve
ser comprado, o 'custo total' do churrasco e o preço por pessoa.
Considerando que: 400g por pessoa, preço R$ 82,40/kg
'''
from rich import print
from rich.console import Console
from rich.panel import Panel
console = Console()


class Churrasco:
    def __init__(self, titulo='', qnt_p=0):
        self.grupo = titulo
        self.quantidade_pessoas = qnt_p
        self.preco = 82.40
        self.consumo = 0.4

    def analisar(self):
        self.consumo_total = 0.4 * self.quantidade_pessoas
        self.custo_total = self.consumo_total * self.preco
        self.custo_pessoa = self.custo_total / self.quantidade_pessoas
        placa = Panel(f'Analisando [bright_cyan]{self.grupo}[/] com [purple]{self.quantidade_pessoas} convidados[/].'
                      f'\nCada participanete comerá {self.consumo}Kg e cada Kg custa R$ {self.preco}.'
                      f'\nRecomenao comprar [purple]{self.consumo_total:.3f}kg[/] de carne.'
                      f'\nO consumo total será de [bright_cyan]R${self.custo_total:.2f}[/].'
                      f'\nCada pessoa pagará [red]R${self.custo_pessoa:.2f}[/].', title=self.grupo, width=70)
        return console.print(placa)


grupo1 = Churrasco('Churras', 3)
grupo1.analisar()
