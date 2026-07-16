from ex033_HEA import *
from rich import inspect, print


def main():
    a1 = Aluno('Mario', 2000, 'ADM')
    a1.nascimento = 2000
    a1.add_curso('Moda')
    inspect(a1, private=True, methods=True)


if __name__ == '__main__':
    main()
