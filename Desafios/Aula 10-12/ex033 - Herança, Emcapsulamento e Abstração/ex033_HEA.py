'''
Implemente a seguinte estrutura de diagrama de classes.

Classe
________________________
Pessoa: {abstract}
________________________
# _nome
# _nascimento
+ @nascimento
+ @idade
________________________
________________________

Subclasse
________________________
Aluno
________________________
+ cursos_oficiais
# _curso
+ @curso
________________________
+ add_curso(curso)
________________________
'''
from abc import ABC
from rich import print, inspect
from datetime import datetime, date


class Pessoa(ABC):
    def __init__(self, nome, nascimento):
        self._nome = nome
        self._nascimento = nascimento

    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self, ano):

        if date.today().year-100 <= ano <= date.today().year:
            self._nascimento = ano
            return self._nascimento
        else:
            raise ValueError('Ano inválido')

    @property
    def idade(self):
        return date.today().year - self._nascimento


class Aluno(Pessoa):
    def __init__(self, nome, nascimento, curso=None):
        super().__init__(nome, nascimento)
        self.curso_oficiais = ['ADM', 'ADS', 'ENG']
        self._curso = curso

    @property
    def curso(self):
        if self._curso not in self.curso_oficiais:
            print('Não encontrado')
        else:
            print(f'Curso {self._curso} Encontrado!')
        return self._curso

    @curso.setter
    def curso(self, curso):
        if curso not in self.curso_oficiais:
            print(f'Curso {curso} não encontrado!')
            return self._curso
        else:
            print('Encontrado!')

    def add_curso(self, curso):
        if len(curso) <= 5:
            self.curso_oficiais.append(curso)
        else:
            print(
                f'{curso} é inválido. Tamanho inapropriado, manter no maximo 5 caracteres.')

