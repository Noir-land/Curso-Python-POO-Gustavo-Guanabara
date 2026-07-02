from rich import print
from rich.panel import Panel
from rich.table import Table
from rich import inspect
from rich.traceback import install
install()

''' 
mostrar todos os emojis cadasrados dentro de biblioteca
python -m rich.emoji
'''


def divisao(x, y):
    return x/y


print('olá, :right_arrow: [bold red on yellow]Mundo[/] :+1:')

caixa = Panel('TESTE de Panel', title='Painel', style='green', width=30)
print(caixa)

tabela = Table(title='Tabela de preços')

tabela.add_column('Nome ', justify='left')
tabela.add_column('Valor ', justify='center')
tabela.add_row('Arroz', 'R$ 50.00')
tabela.add_row('Bolo de Chocolate', 'R$ 190.00')

print(tabela)

inspect(len) # all=True  para mostrar todas informações

print(divisao(4,0))