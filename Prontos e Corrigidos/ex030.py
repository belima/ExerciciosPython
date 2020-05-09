'''Crie um programa que leia um número e informe se ele é par ou ímpar.'''

n = int(input('Digite um número:\n>>> '))

print('{} é {}!'.format(n, 'par' if n % 2 == 0 else 'ímpar'))
