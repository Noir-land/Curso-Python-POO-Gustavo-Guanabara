from ex025 import *
from rich.table import Table


def main():

    distancia = 100
    entrega = Moto(distancia)
    print(
        f'Frete de {type(entrega).__name__} na distancia de {distancia}Km = {entrega.calc_frete()}')

    fretes = [Moto(distancia), Caminhao(distancia), Drone(distancia)]
    tabela = Table()
    tabela.add_column('Distância')
    tabela.add_column('Tipo')
    tabela.add_column('frete')
    for i, n in enumerate(fretes):
        tabela.add_row(f'{distancia}Km', type(
            fretes[i]).__name__, fretes[i].calc_frete())

    print(tabela)


if __name__ == '__main__':
    main()
