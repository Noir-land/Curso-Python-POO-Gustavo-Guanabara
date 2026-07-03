from ex029_Diario import *


def main():
    pessoa = Diario()
    pessoa.escrever('olá')
    pessoa.escrever('GEm')
    try:
        pessoa.ler(123)
    except Exception as e:
        print(f'{e}')

    pessoa.senha()
     
    pessoa.ler()
   
    
if __name__ == '__main__':
    main()
