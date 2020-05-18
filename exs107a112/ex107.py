'''
crie um modulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
faça tb um programa que importe esse módulo e use algumas dessas funções.
'''
from utilidadesCeV import moeda

valor = float(input('Digite o preço: R$'))

print(f"A metade de R${valor} é R${moeda.metade(valor)}")
print(f"O dobro de R${valor} é R${moeda.dobra(valor)}")
print(f"Aumentando 200% temos R${moeda.aumentar(valor, 200)}")
print(f"Descontando 50% temos R${moeda.diminuir(valor, 50)}")
