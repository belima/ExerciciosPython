'''
gere 5 numeros aleatórios e guarde numa tupla.
mostre a listagem de numeros gerados e indique o maior e o menor numeros armazenados
'''
from random import randint

tupla = randint(0, 999), randint(0, 999), randint(0, 999), randint(0, 999), randint(0, 999)

print(f'Os numeros gerados foram {tupla}')
print(f'O maior numero foi {max(tupla)} e o menor {min(tupla)}.')
