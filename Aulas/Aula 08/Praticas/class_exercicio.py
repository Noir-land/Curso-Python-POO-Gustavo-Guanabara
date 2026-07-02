from abc import ABC, abstractmethod  # Abstract Base Classes
from rich import inspect

class Pessoa(ABC):
    def __init__(self, nome='', idade=0):
        self.nome = nome
        self.idade = idade

    def aniversario(self):
        self.idade += 1

    @abstractmethod
    def estudar(self):
        pass


class Aluno(Pessoa):
    def __init__(self, nome='', idade=0, curso='', turma=''):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f'Matricula de {self.nome} foi concluida.')

    def estudar(self):
        print(
            f'Aluno {self.nome} está estudando {self.curso} na turma {self.turma}')


class Professor(Pessoa):
    def __init__(self, nome='', idade=0, especialidade='', nivel=''):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(
            f'O professor {self.nome} de {self.idade} anos, tem especialidade em {self.especialidade}, de grau {self.nivel}.')

    def estudar(self):
        print(
            f'O professor {self.nome} faz auto estudo em {self.especialidade}')


class Funcionario(Pessoa):
    def __init__(self, nome='', idade=0, cargo='', setor=''):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(f'A funcionaraia {self.nome}, acabou de bater ponto.')

    def estudar(self):
        print(
            f'O funcionario {self.nome} mantém um estudo para se especializar na área {self.setor}')
