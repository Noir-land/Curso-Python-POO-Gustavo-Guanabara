'''
Crie a classe ControleRemoto, onde vamos 'simular' o funcionamento de um
controle simples(canal, volume e ligar/desligar)
'''
from rich.traceback import install
from rich.panel import Panel
from rich import print
from rich.console import Console
console = Console()
install()


class ControleRemoto:
    def __init__(self):
        self.On_Off = False
        self.canais = [1, 2, 30, 25, 5]
        self.volume = 1
        self.canal_atual = 3

    def tv(self, msg=''):
        if self.On_Off:
            linhas = [f'[black on red] {self.canais[k]} [/]' if x == self.canais[self.canal_atual]
                      else f'{x}' for k, x in enumerate(self.canais, start=0)]

            self.caixa = Panel(f'CANAL = {" ".join(linhas)} \nVOLUME = {':green_square:'*(self.volume)} ',
                               title='[TV]', width=30)
            return console.print(self.caixa), self.comando()
        else:
            self.caixa = Panel(
                '[red]A TV está Desligada[/]', title='[TV]', width=30)
            return console.print(self.caixa), self.comando()

    def comando(self, msg=''):
        msg = input(
            f'< CH-{self.canais[self.canal_atual]} >   - VOL-{self.volume} + ')
        while True:
            if self.On_Off == False:
                if msg == '@':
                    self.On_Off = True
                    return self.tv()
            else:
                if msg == '@':
                    self.On_Off = False
                    return self.tv()
                if msg in '-+' and self.volume <= 3:
                    if msg == '+' and self.volume < 3:
                        self.volume += 1
                        return self.tv()

                    elif msg == '-':
                        if self.volume > 1:
                            self.volume -= 1
                            return self.tv()
                        else:
                            return self.tv()
                    else:
                        return self.tv()
                elif msg in '<>':
                    if msg == '>':
                        if self.canal_atual == len(self.canais)-1:
                            self.canal_atual = 0
                            return self.tv()
                        else:
                            self.canal_atual += 1
                            return self.tv()
                    elif msg == '<':
                        if self.canal_atual == 0:
                            self.canal_atual = len(self.canais)-1
                            return self.tv()
                        else:
                            self.canal_atual -= 1
                            return self.tv()
                else:
                    return self.tv()


pessoa1 = ControleRemoto()
pessoa1.tv()
pessoa1.comando()
