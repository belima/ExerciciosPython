'''
modifique as funções que foram criadas no ex107 para que elas aceitem um parâmetro a mais, informando se o valor
retornado vai ou não ser formatado pela função moeda(), desenvolvida no ex108.
'''
from utilidadesCeV import moeda

valor = float(input('Digite o preço: R$'))

print(f"A metade de {moeda.moeda(valor)} é {moeda.metade(valor, din=True)}")
print(f"O dobro de {moeda.moeda(valor)} é {moeda.dobra(valor, din=True)}")
print(f"Aumentando 10% temos {moeda.aumentar(valor, 10, din=True)}")
print(f"Descontando 13% temos {moeda.diminuir(valor, 13, din=True)}")