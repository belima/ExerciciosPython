'''
Faça um mini-sistema que utilize o Interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparecer.
Qd o usuário digitar 'FIM' o programa se encerrará. Use cores.
'''
from time import sleep


def seção(msg, fundo='default'):
    cores = {'default': '\033[m',
             'vermelho': '\033[30;41m',
             'verde': '\033[30;42m',
             'azul': '\033[30;44m',
             'branco': '\033[30;7m'}

    print(cores[fundo], end='')
    print('~' * (len(msg) + 4))
    print(f"  {msg}  ")
    print('~' * (len(msg) + 4))
    print(cores['default'],end='')


def consulta(cmd):
    print('\033[30;7m', end='')
    help(cmd)
    print('\033[m', end='')


while True:
    seção('SISTEMA DE AJUDA PyHELP', 'verde')
    sleep(0.5)
    entrada = str(input('Função ou Biblioteca > '))
    if entrada.strip().upper() == 'FIM':
        sleep(0.5)
        break
    seção(f"Acessando o manual do comando '{entrada}'", fundo='azul')
    sleep(0.5)
    consulta(entrada)
    sleep(0.5)
seção('ATÉ LOGO!', fundo='vermelho')