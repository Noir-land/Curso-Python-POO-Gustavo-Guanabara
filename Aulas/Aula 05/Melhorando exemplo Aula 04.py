<<<<<<< HEAD
# Declaração de classe
class Gafanhoto:
    def __init__(self, nome='', idade=0):  # Metodo construtor
        # Atributo de instância
        self.nome = nome
        self.idade = idade

    # Metodo de instância
    def aniversario(self):
        self.idade = self.idade + 1

    def mensagem(self):
        return f'{self.nome} tem {self.idade} anos'
    
    # Dunner Methor. Fara uma chamada personalizada para mostrar o endereço do metodo na memoria, desta forma, não é necessario a requisição do def mensagem
    def __str__(self):     
        return f'O {self.nome} tem {self.idade} anos'

    def __getstate__(self):
        return f'Estado: nome = {self.nome} ; idade = {self.idade}'
# Declaração de objetos


g1 = Gafanhoto('Noir', 50)
g1.aniversario()
print(g1)
print(g1.__dict__) # Atributo / Attribute
print(g1.__getstate__()) #Metodo / Method 
print(g1.__class__) # Para saber à qual classe deste objeto


g2 = Gafanhoto('Scrin')
g2.aniversario()
print(g2.mensagem())


'''
Dunner Dicts: __dict__ exibira as informações dos atributos em forma de dicionario, e 
 __getstate__(), pode ser usado para o mesmo resultado, mas com a opção de modificar o resultado
'''
=======
# Declaração de classe
class Gafanhoto:
    def __init__(self, nome='', idade=0):  # Metodo construtor
        # Atributo de instância
        self.nome = nome
        self.idade = idade

    # Metodo de instância
    def aniversario(self):
        self.idade = self.idade + 1

    def mensagem(self):
        return f'{self.nome} tem {self.idade} anos'
    
    # Dunner Methor. Fara uma chamada personalizada para mostrar o endereço do metodo na memoria, desta forma, não é necessario a requisição do def mensagem
    def __str__(self):     
        return f'O {self.nome} tem {self.idade} anos'

    def __getstate__(self):
        return f'Estado: nome = {self.nome} ; idade = {self.idade}'
# Declaração de objetos


g1 = Gafanhoto('Noir', 50)
g1.aniversario()
print(g1)
print(g1.__dict__) # Atributo / Attribute
print(g1.__getstate__()) #Metodo / Method 
print(g1.__class__) # Para saber à qual classe deste objeto


g2 = Gafanhoto('Scrin')
g2.aniversario()
print(g2.mensagem())


'''
Dunner Dicts: __dict__ exibira as informações dos atributos em forma de dicionario, e 
 __getstate__(), pode ser usado para o mesmo resultado, mas com a opção de modificar o resultado
'''
>>>>>>> 95efe2e4a3517c83285284c5daa26799496ee1f6
