from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome='', idade=0, curso='', turma=''):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f'Matricula de {self.nome} foi concluida.')