''' leia o primeiro termo e a razão de uma PA. Mostre os 10 primeiros termos dessa progressão'''

inicio = int(input('Qual o primeiro termo da PA? '))
razao = int(input('Qual a razão da PA? '))


termo = inicio
print('Os dez primeiros termos dessa PA são', end='')
for c in range(0, 10):
    print(' {},'.format(termo),end='')
    termo += razao
print(' ...')

'''
ult = inicio + 9 *razao
print('Os dez primeiros termos dessa PA são', end='')
for c in range(inicio, ult + 1, razao):
    print(' {},'.format(c),end='')
print(' ...')
'''

