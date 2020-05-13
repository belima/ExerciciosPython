"""
leia 5 valores numericos e guarde em uma lista.
mostre quais foram o maior e o menor valores digitados e suas respectivas posições na lista.
"""

lista = []
for i in range(0,5):
    lista.append(int(input(f'Digite um número para a posição {i}: ')))

print('~' * 40)
print(f'Você digitou os valores {lista}')
print(f'O menor valor digitado foi {min(lista)}, na(s) posição(ões) ',end='')
for i, v in enumerate(lista):
    if v == min(lista):
        print(f'{i}... ',end='')
print()
print(f'O maior valor digitado foi {max(lista)}, na(s) posição(ões) ',end='')
for i, v in enumerate(lista):
    if v == max(lista):
        print(f'{i}... ',end='')
print()
