'''
Crie a classe Gamer, onde podemos cadastrar 'nome', 'nick' e 'jogos favoritos' de uma pessoa.
Crie também um método que permita 'mostrar a ficha' desse gamer.
'''
from rich import print
from rich.panel import Panel
from rich.console import Console
console = Console()


class Gamer:
    def __init__(self, nome='', nick=''):
        self.nome = nome
        self.nick = nick
        self.jogos = list()

    def add_favoritos(self, jogos=''):
        self.jogos.append(jogos)
        self.jogos.sort()  # self.jogos = sorted(self.jogos, key=str.lower)

    def ficha(self):
        x = Panel(
            f'Nome real:[bold white on red ] {self.nome} [/] \nJogos favoritos:\n[blue]:video_game: {'\n:video_game: '.join(f'{x}'for x in self.jogos)}[/]', title=f'Jogador <{self.nick}>', width=40)
        return console.print(x)


j1 = Gamer('Lucas', 'Noir')
j1.add_favoritos('TESO')
j1.add_favoritos('Mortal')
j1.add_favoritos('PW')
j1.ficha()


j2 = Gamer('Jorge', 'dasmal15877')
j2.add_favoritos('nfs')
j2.add_favoritos('bf')
j2.ficha()
