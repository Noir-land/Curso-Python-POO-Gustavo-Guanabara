from Avaliação_Getters_Setters import *
from rich import print


def main():
    aluno = Avaliacao('Juremitiza', 'Inglês', 8.5)
    aluno.set_nota(5)
    print(f'{aluno.nome} tirou nota: {aluno.get_nota()} na disciplina {aluno.disciplina}')

if __name__ == '__main__':
    main()
