from ex030_Criptografia import *


def main():
    pessoa = Credencial()
    pessoa.senha = ''
    senha = getpass('Digite a senha: ', echo_char='*')
    pessoa.validar(senha)


if __name__ == '__main__':
    main()
