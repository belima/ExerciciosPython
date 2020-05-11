'''
jogue par ou ímpar com o computador.
o jogo segue até que o usuário perca, mostrando, ao final
o total de vitórias consecutivas conquistadas.
'''
from random import randint

cont = 0
barrinha = '-=' * 20
separatil = '~' * 40

print(barrinha)
print(f'{"PAR ou ÍMPAR?!":^40}')

while True:
    pc = randint(0, 5)

    print(barrinha)
    while True:
        parouimpar = str(input('Par ou ímpar? [P/I] > ')).upper().strip()[0]
        if parouimpar in 'PI':
            break
    while True:
        usr = int(input('Quantos dedos? [0-5] > '))
        if 0 <= usr <= 5:
            break

    soma = pc + usr
    if soma % 2 == 0:
        result = 'PAR'
    else:
        result = 'ÍMPAR'
    print(separatil)
    print(f'Você botou {usr} e eu botei {pc}! {soma} é {result}!')
    print(separatil)

    if  result == 'PAR' and parouimpar == 'P' or result == 'ÍMPAR' and parouimpar == 'I':
        print('Você venceu!\nBora de novo!')
        cont += 1
    else:
        if cont > 1:
            print(f'Você perdeu depois de {cont} vitórias!')
        elif cont == 1:
            print('Você perdeu depois de 1 vitória!')
        else:
            print('Você perdeu!')
        break
