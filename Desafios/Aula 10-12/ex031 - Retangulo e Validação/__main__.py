from ex031_Retangulo_Validacao import *


def main():
    r = Retangulo()
    r.altura = -4
    r.base = -3

    print(r.medidas)
    inspect(r, private=True, methods=True)


if __name__ == '__main__':
    main()
