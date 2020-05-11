'''
refaça o ex051 (PA), mostrando os 10 primeiros termos, usando while.

ex051:
leia o primeiro termo e a razão de uma PA. Mostre os 10 primeiros termos dessa progressão
'''

inicio = int(input('Qual o primeiro termo da PA? '))
razao = int(input('Qual a razão da PA? '))


termo = inicio
c = 0
print('Os dez primeiros termos dessa PA são', end='')
while c < 10:
    print(' {},'.format(termo),end='')
    termo += razao
    c += 1
print('...')
