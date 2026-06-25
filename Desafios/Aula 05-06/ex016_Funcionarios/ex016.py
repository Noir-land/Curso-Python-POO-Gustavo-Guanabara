'''
Crie a classe Funcionario, onde podemos cadastrar 'nome', 'setor' e cargo.
Crie também um método que permita ao funcioário se apresentar.
'''
from rich import print


class Funcionario:
    # Atributos de classe
    empresa = 'Fulano de tal'

    def __init__(self, nome='', setor='', cargo=''):
        # Atributos de instância
        self.funcionario = nome
        self.area_trabalho = setor
        self.cargo = cargo

    def apresentar(self):
        return f'O funcionario [blue]{self.funcionario}[/], trabalha no setor {self.area_trabalho} com o cargo de {self.cargo} na empresa {Funcionario.empresa}'

# altera a empresa que esta no Atributo de classe
# Funcionario.empresa=' nem sei'


trabalhador1 = Funcionario('João', 'Admnistração', 'Estagiario')


# cria um atributo novo em local
# trabalhador1.empresa = 'Não sei'


print(trabalhador1.apresentar())
