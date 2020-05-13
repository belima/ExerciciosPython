'''
leia 7 valores numericos e cadastre em uma unica lista que mantenha, separadamente,
os valores pares e os ímpares.
mostre os valores pares e ímpares em ordem crescente
'''

valores = [[], []]

for i in range(0, 7):
    n = int(input(f'{i + 1}º valor > '))
    valores[n % 2].append(n)

print('~~' * 30)
print(f'Os valores pares digitados foram {sorted(valores[0])} e os ímpares {sorted(valores[1])}')
