'''
adapte o código do ex107 criando uma função adicional chamada moeda() que consiga mostrar os valores como um valor
monetário formatado.
'''
import moeda

valor = float(input('Digite o preço: R$'))

print(f"A metade de {moeda.moeda(valor)} é {moeda.moeda(moeda.metade(valor))}")
print(f"O dobro de {moeda.moeda(valor)} é {moeda.moeda(moeda.dobra(valor))}")
print(f"Aumentando 200% temos {moeda.moeda(moeda.aumentar(valor, 200))}")
print(f"Descontando 50% temos {moeda.moeda(moeda.diminuir(valor, 50))}")