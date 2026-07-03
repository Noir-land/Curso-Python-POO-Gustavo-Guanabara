from Avaliação_Property import *
from rich import print, inspect


def main():
    aluno = Avaliacao('Juremitiza', 'Inglês', 8.5)
    aluno.nota = 5
    print(f'{aluno.nome} tirou nota: {aluno.nota} na disciplina {aluno.disciplina}')
    inspect(aluno, private=True)
if __name__ == '__main__':
    main()
