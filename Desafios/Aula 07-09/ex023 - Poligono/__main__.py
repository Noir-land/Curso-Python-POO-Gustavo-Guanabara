from ex023 import*
from rich import print

def main():
    p1 = Circulo(20)
    p2 = Quadrado(20)
    print(f'Um quadrado de {p2.qnt_lados}cm perímetro é de {p1.perimetro():.1f} cm e a área é de {p1.area():.1f} cm²')
    print(f'Um Circulo de {p1.raio}cm perímetro é de {p2.perimetro():.1f} cm e a área é de {p2.area():.1f} cm²')

if __name__ == '__main__':
    main()