'''
adicione ao modulo moeda.py uma função chamada resumo() q mostre na tela algumas informações geradas pelas funções
que já temos no módulo criado até aqui.
'''
from utilidadesCeV import moeda

v = float(input('Digite o valor > '))
a = float(input('Acrescimo > '))
d = float(input('Desconto > '))

moeda.resumo(v, a, d)


