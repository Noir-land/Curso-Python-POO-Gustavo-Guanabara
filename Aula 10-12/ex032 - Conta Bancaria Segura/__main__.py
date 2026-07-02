from ex032_ContaBancariaSegura import *


def main():

    pessoa = ContaBancaria(123, 'CRk', 1000, 'brito')
    pessoa.sacar(500)
    pessoa.depositar()
    inspect(pessoa, private=True, methods=True)


if __name__ == '__main__':
    main()
