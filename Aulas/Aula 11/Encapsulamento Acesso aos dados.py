'''
Metodos acessores, que validam se o que foi requisitado deve ser executado ou não
Existem duas maneiras de permitir o acesso aos dados encapsuados:

Uso de getters e setters
Uso de decorador @property

Exemplos de funcionamento de getters e setters:

Classe
______________________
Avaliacao
______________________
+ nome
+ disciplina 
# _nota 
______________________
+ set_nota(valor)
+ get_nota()
______________________

def main():
    a = Avaliacao()
    a.nome = 'Jurema'
    a.disciplina = 'Inglês'
    a.set_nota(8.5)

    
Exemplo de funcionamento de @property

Classe
______________________
Avaliacao
______________________
+ nome
+ disciplina
# _nota
+ @nota.getter
+ @nota.setter
______________________
______________________

'''