from pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome='', idade=0, especialidade='', nivel=''):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f'O professor {self.nome} de {self.idade} anos, tem especialidade em {self.especialidade}, de grau {self.nivel}.')