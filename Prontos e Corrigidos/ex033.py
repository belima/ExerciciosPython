'''Escreva um programa que leia 3 números e mostre qual é o maior e qual é o menor'''

print('\n\n-=|Compara Números|=-\n')

a = float(input('Primeiro número: '))
b = float(input('Segundo número: '))

if a < b:
    menor = a
    maior = b
else:
    if a > b:
        maior = a
        menor = b
    else:
        maior = menor = a

c = float(input('Terceiro número: '))

if c < menor:
    menor = c
if c > maior:
    maior = c

if a == b == c:
    print('\nVocê digitou três números iguais!')
else:
    print('\nO menor número digitado foi {} e o maior foi {}'.format(menor, maior))
