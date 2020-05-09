'''
leia dois valores e depois mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] ler novos numeros
[5] sair do programa
'''

validas = (1, 2, 3, 4, 5)           # define opções válidas no menu

print('Entre com os valores:')
v1 = float(input('Valor 1 > '))     # lê valores
v2 = float(input('Valor 2 > '))

maior = v1
if v2 > v1:                 # verifica maior valor
    maior = v2

sel = int(0)

while sel not in validas:                      # exibe menu enquanto opção selecionada não for válida
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
        sel = 0
    elif sel == 2:
        print('{} * {} = {}'.format(v1, v2, v1 * v2))
        sel = 0
    elif sel == 3:
        if v1 == v2:
            print('Os dois valores são iguais. {}'.format(v1))
            sel = 0
        else:
            print('{} é o maior valor.'.format(maior))
            sel = 0
    elif sel == 4:
        v1 = int(input('Valor 1 > '))
        v2 = int(input('Valor 2 > '))
        sel = 0
    elif sel == 5:
        print('Até a próxima =)')
