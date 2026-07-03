from ex030_Criptografia import *


def main():
    pessoa = Credencial()
    pessoa.senha = 'ola'
    pessoa.validar('a')


if __name__ == '__main__':
    main()
