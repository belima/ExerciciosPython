'''
melhore o ex061 perguntando se o usuario deseja ver mais termos. O programa encerra quando o usuário digitar 0.

ex061:
refaça o ex051 (PA), mostrando os 10 primeiros termos, usando while.

ex051:
leia o primeiro termo e a razão de uma PA. Mostre os 10 primeiros termos dessa progressão
'''

inicio = int(input('Qual o primeiro termo da PA?\n> '))
razao = int(input('Qual a razão da PA?\n> '))


termo = inicio
c = 10
print('Os dez primeiros termos dessa PA são:')

while c > 0:
    if c > 2:
        print(' {},'.format(termo),end='')
        termo += razao
        c -= 1
    elif c == 2:
        print(' {} e'.format(termo), end='')
        termo += razao
        c -= 1
    elif c == 1:
        print(' {}.'.format(termo), end='')
        termo += razao
        c -= 1

i = int(1)
while i != 0:
    i = int(input('\nGostaria de ver mais quantos termos? (0 para sair)\n> '))
    c = i
    if i != 0:
        if c > 1:
            print('Os {} termos seguintes dessa PA são:'.format(c))
        elif c == 1:
            print('O termo seguinte dessa PA é:')

        while c > 0:
            if c > 2:
                print(' {},'.format(termo), end='')
                termo += razao
                c -= 1
            elif c == 2:
                print(' {} e'.format(termo), end='')
                termo += razao
                c -= 1
            elif c == 1:
                print(' {}.'.format(termo), end='')
                termo += razao
                c -= 1

print('\nAté a próxima!')
