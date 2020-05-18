'''
Faça um mini-sistema que utilize o Interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparecer.
Qd o usuário digitar 'FIM' o programa se encerrará. Use cores.
'''
from time import sleep
cores = {'default': '\033[m',
         'vermelho': '\033[30;41m',
         'verde': '\033[30;42m',
         'azul': '\033[30;44m',
         'branco': '\033[30;7m'}


def titulo(msg, fundo='default'):
    print(cores[fundo], end='')
    print('~' * (len(msg) + 4))
    print(f"  {msg}  ")
    print('~' * (len(msg) + 4))
    print(cores['default'], end='')
    sleep(0.5)


def consulta(cmd):
    titulo(f"Acessando o manual do comando '{cmd}'", fundo='azul')
    print(cores['branco'], end='')
    help(cmd)
    print(cores['default'], end='')
    sleep(0.5)


# main
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 'verde')
    sleep(0.5)
    entrada = str(input('Função ou Biblioteca > '))
    if entrada.strip().upper() == 'FIM':
        sleep(0.5)
        break
    consulta(entrada)
titulo('ATÉ LOGO!', fundo='vermelho')