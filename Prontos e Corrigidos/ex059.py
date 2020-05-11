'''
leia dois valores e depois mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] ler novos numeros
[5] sair do programa
'''
from time import sleep

print('Entre com os valores:')
v1 = float(input('Valor 1 > '))     # lê valores
v2 = float(input('Valor 2 > '))

sel = int(0)

while sel != 5:                      # exibe menu enquanto opção selecionada não for válida
    print('''\nSelecione a opçao desejada
--------------------------
[ 1 ] Soma
[ 2 ] Multiplicação
[ 3 ] Maior valor
[ 4 ] Ler novos valores
[ 5 ] Sair''')

    sel = int(input('>>> '))

    if sel == 1:                                            # executa opção selecionada
        print('{} + {} = {}'.format(v1, v2, v1 + v2))
    elif sel == 2:
        print('{} * {} = {}'.format(v1, v2, v1 * v2))
    elif sel == 3:
        if v1 == v2:
            print('Os dois valores são iguais. {}'.format(v1))
        else:
            if v2 > v1:
                maior = v2
            if v1 > v2:
                maior = v1
            print('{} é o maior valor.'.format(maior))
    elif sel == 4:
        v1 = float(input('Valor 1 > '))
        v2 = float(input('Valor 2 > '))
    elif sel == 5:
        print('Até a próxima =)')
    else:
        print('<< Opção inválida >>')
    sleep(1)
