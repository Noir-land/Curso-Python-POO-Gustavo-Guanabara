'''
Crie a classe Livro, que vai simulara passagem de páginas de um livro,
considerando também se o usuário chegou ao fim da leitura.
'''
from rich import print


class Livro:
    def __init__(self, titulo='', paginas=0):
        self.titulo = titulo
        self.paginas = paginas
        self.pagina_atual = 1

    def proxima_pag(self, pagina=0):
        self.pagina_avanca = pagina
        if self.pagina_atual == 1:
            print(
                f'[purple]Você acabou de abrir o livro [bold red]{self.titulo}[/] que contém {self.paginas} paginas[/].')
            print(
                f'[bright_cyan]Você esta atualmente na [/][bright_green]página {self.pagina_atual}[/]')
        cont = 1
        while True:
            if cont > self.pagina_avanca:
                print(
                    f'[bright_cyan]Você avançou {cont-1} paginas. Você esta atualmente na [/][bold bright_green]Pág {self.pagina_atual}[/]', end=' ')
                break
            elif self.pagina_atual < self.paginas:
                self.pagina_atual += 1
                cont += 1
                print(f'Pág{self.pagina_atual}', end=' ► ')
            else:
                print(
                    f'[bright_cyan]Você avançou {cont-1} páginas. Você esta atualmente na [/][bright_green]Pág {self.pagina_atual}[/]', end=' ')
                print(
                    f'\n[red]Você chegou ao final do livro {self.titulo}. [/]')
                break


livro = Livro('Eis que não sei', 20)
livro.proxima_pag(7)
livro.proxima_pag(4)
livro.proxima_pag(15)

