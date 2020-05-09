'''Escreva um programa que faça o computador pensar em um numero inteiro entre 0 e 5 e peça para o usuário
tentar descobrir o número escolhido.
O programa deverá informar se o usuário venceu ou perdeu.'''
from random import randint
from time import sleep

print('\n\033[1;31m{:^50}\033[m'.format('==|Chutaí!|=='))
print('\033[1;31m-\033[m' * 50)
pens = int(randint(0,5)) # Sorteia um numero

print('\nOlá! Estou pensando em um número inteiro entre 0 e 5!')

chute = int(input('Adivinha qual é?!\n>>> '))

print('Processando...')
sleep(1)

if chute == pens:
    print('\033[1;32mAcertou Miseravi!!!\033[m Eu tava pensando no {} mesmo! =D'.format(pens))
else:
    print('\033[1;31mVish, errou!!\033[m '
          'Eu tava pensando no {}! :p'.format(pens))
