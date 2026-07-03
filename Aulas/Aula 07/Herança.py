from rich import inspect, print


class Pessoa:
    def __init__(self, nome='', idade=0):
        self.nome = nome
        self.idade = idade

    def aniversario(self):
        self.idade += 1


class Aluno(Pessoa):
    def __init__(self, nome='', idade=0, curso='', turma=''):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f'Matricula de {self.nome} foi concluida.')


class Professor(Pessoa):
    def __init__(self, nome='', idade=0, especialidade='', nivel=''):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f'O professor {self.nome}, tem especialidade em {self.especialidade}, de grau {self.nivel}.')


class Funcionario(Pessoa):
    def __init__(self, nome='', idade=0, cargo='', setor=''):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(f'A funcionaraia {self.nome}, acabou de bater ponto.')


a1 = Aluno('Hélio', 20, 'Informática', 'T12')
a1.fazer_matricula()

p1 = Professor('Jair', 48, 'Matemática', 'Mestrado')
p1.dar_aula()

f1 = Funcionario('Maria', 'Gerente', 'Alimentar' )
f1.bater_ponto()

