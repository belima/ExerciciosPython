'''
crie um pacote chamado utilidadesCeV que tenha dois modulos internos chamados moeda e dado.
Transfira todas as funções utilizadas nos ex de 107 a 110 para o primeiro pacote (moeda) e mantenha tudo funcionando
'''
from utilidadesCeV import moeda

v = float(input('Digite o valor > '))
a = float(input('Acrescimo > '))
d = float(input('Desconto > '))

moeda.resumo(v, a, d)