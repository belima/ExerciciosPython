'''Escreva um programa que leia 3 números e mostre qual é o maior e qual é o menor'''

print('\n\n-=|Compara Números|=-\n')

a = float(input('Primeiro número: '))
b = float(input('Segundo número: '))
c = float(input('Terceiro número: '))

menor = a
maior = c

if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

if a > c and a > b:
    maior = a
if b > c and b > a:
    maior = b

if a == b == c:
    print('Você digitou três números iguais!')
else:
    print('O menor valor digitado foi {} e o maior foi {}.'.format(menor, maior))
