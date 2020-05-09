'''
melhore o jogo do ex028 (comp pensa um numero de 1 a 10).
Dessa vez o jogador tentará adivinhar até acertar, mostrando no final quantas tentativas foram necessárias.

ex028:
Escreva um programa que faça o computador pensar em um numero inteiro entre 0 e 5 e peça para o usuário
tentar descobrir o número escolhido.
O programa deverá informar se o usuário venceu ou perdeu.
'''


from random import randint
from time import sleep

print('\n\033[1;31m{:^50}\033[m'.format('==|Chutaí!|=='))
print('\033[1;31m-\033[m' * 50)
pens = int(randint(0,5)) # Sorteia um numero

print('\nOlá! Estou pensando em um número inteiro entre 0 e 5!')

chute = int(input('Adivinha qual é?!\n>>> '))
print('Processando...')
sleep(0.3)

while chute != pens:
    print('\033[1;31mErrrrou!!\033[m')
    chute = int(input('Tenta de novo!\n>>> '))
    print('Processando...')
    sleep(0.3)

if chute == pens:
    print('\033[1;32mAcertou Miseravi!!!\033[m Era {} mermo! =D'.format(pens))
