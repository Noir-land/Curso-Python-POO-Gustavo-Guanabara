"""
Crie a estrutura capaz de 'calcular salário' de funcionários diferentes

Classe
________________________________________
Funcionario {abstract}
________________________________________
+ nome
+ sal_bruto
+ salario
+ sal_min = 1612
+ inss = 7.5
________________________________________
+ calc_sal() {abstract}
+ analisar_sal()
________________________________________

SubClasse
________________        ________________
Mensalista                |Mensalista
________________       |________________
+ valor_hora           | 
+ horas_trab           |             
________________       |________________
+ calc_sal()           |+ calc_sal()
________________       |________________
"""

from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel


class Funcionario(ABC):
    def __init__(self, nome, salario):
        self.nome = nome
        self.sal_bruto = salario
        self.salario = 0
        self.sal_minimo = 1612
        self.inss = 7.5

    @abstractmethod
    def cal_sal():
        pass

    def analisar_sal(self):
        painel = Panel(
            f'O salario de {self.nome}({self.__class__.__name__}) é de R${self.salario:.2f} e corresponde a {self.salario/self.sal_minimo:.1f} salários minimos', title='Análise de Salário', width=50)
        print(painel)


class Horista(Funcionario):
    def __init__(self, nome, salario=0, valor=7.5, hrs=220):
        super().__init__(nome, salario)
        self.valor_hora = valor
        self.horas_trab = hrs

    def cal_sal(self):
        self.sal_bruto = (self.valor_hora * self.horas_trab)
        self.salario = self.sal_bruto - (self.sal_bruto * self.inss / 100)
        return self.salario

    def analisar_sal(self):
        return Funcionario.analisar_sal(self)


class Mensalista(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)

    def cal_sal(self):
        self.salario = self.sal_bruto - (self.sal_bruto * self.inss / 100)
        return self.salario

    def analisar_sal(self):
        return Funcionario.analisar_sal(self)
