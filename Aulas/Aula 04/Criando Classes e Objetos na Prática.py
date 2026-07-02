# Declaração de classe
class Gafanhoto:
    def __init__(self):  # Metodo construtor
        # Atributo de instância
        self.nome = ''
        self.idade = 0

    # Metodo de instância
    def aniversario(self):
        self.idade = self.idade + 1

    def mensagem(self):
        return f'{self.nome} tem {self.idade} anos'
# Declaração de objetos

g1 = Gafanhoto()
g1.nome = 'Noir'
g1.idade = 50
g1.aniversario()
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = 'Scrin'
g2.aniversario()
print(g2.mensagem())