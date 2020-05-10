'''
melhore o jogo do ex028 (comp pensa um numero de 1 a 10).
Dessa vez o jogador tentará adivinhar até acertar, mostrando no final quantas tentativas foram necessárias.

ex028:
Escreva um programa que faça o computador pensar em um numero inteiro entre 0 e 5 e peça para o usuário
tentar descobrir o número escolhido.
O programa deverá informar se o usuário venceu ou perdeu.
'''

from random import randint

print('\n\033[1;31m{:^50}\033[m'.format('==|Chutaí!|=='))
print('\033[1;31m-\033[m' * 50)
pens = int(randint(0,10))   # Sorteia um numero

print('\nOlá! Estou pensando em um número inteiro entre 0 e 10!')

chute = int(input('Adivinha qual é?!\n>>> '))
tent = 1

while chute != pens:
    print('\033[1;31mErrrrou!!\033[m')
    tent += 1
    if chute > pens:
        chute = int(input('Menos! Tenta de novo!\n>>> '))
    elif chute < pens:
        chute = int(input('Mais! Tenta de novo!\n>>> '))

if chute == pens:
    print('\033[1;32mAcertou Miseravi!!!\033[m Era {} mermo! =D'.format(pens))
    print('Acertou na {}ª tentativa!'.format(tent))
