from ex030_Criptografia import *


def main():
    pessoa = Credencial()
    pessoa.senha = ''
    pessoa.validar(getpass('Digite a senha: ', echo_char='*'))


if __name__ == '__main__':
    main()
