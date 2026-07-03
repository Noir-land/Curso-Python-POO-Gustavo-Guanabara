from ex026 import *

def main():
    f1 = Mensalista('Noir', 9500)
    f1.cal_sal()
    f1.analisar_sal()

    f2 = Horista(nome='Creuza', hrs=220)
    f2.cal_sal()
    f2.analisar_sal()


if __name__ == '__main__':
    main()