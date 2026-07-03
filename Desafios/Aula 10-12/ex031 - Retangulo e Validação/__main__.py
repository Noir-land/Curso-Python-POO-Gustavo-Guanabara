from ex031 import*

def main():
    r = Retangulo()
    r.altura = -4
    r.base = -3

    print(r.medidas)
    inspect(r, private=True, methods=True)