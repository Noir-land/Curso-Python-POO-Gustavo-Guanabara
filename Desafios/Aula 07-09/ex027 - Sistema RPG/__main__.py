from ex027 import *


def main():
    p1 = Guerreiro('Arthur', 3000)
    p2 = Mago('Pato', 2000)
    p2.atacar(p1, 1000)
    p1.atacar(p2, 1000)
    p2.atacar(p1, 3000)
    p1.curar()
    p2.atacar(p1, 1000)


if __name__ == '__main__':
    main()
