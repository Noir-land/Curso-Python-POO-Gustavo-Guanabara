from ex032_ContaBancariaSegura import *


def main():

    pessoa = ContaBancaria(123, 'CRk', 1000)
    pessoa.sacar(500)
    pessoa.depositar(200)
    inspect(pessoa, private=True, methods=True)


if __name__ == '__main__':
    main()
