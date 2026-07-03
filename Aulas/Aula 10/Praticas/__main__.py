from Conta_Bancaria import *

def main():
    pesssoa1 = ContaBancaria(id=112, nome='Hélio', saldo=3000)
    pesssoa1.deposito(-500)
    pesssoa1.sacar(4000)
    print(pesssoa1)



if __name__ == '__main__':
    main()