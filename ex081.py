"""
leia vários numeros e coloque em uma lista.
mostre:
 a) quantos números foram digitados
 b) a lista de valores ordenada de forma decrescente
 c) se o valor 5 foi adicionado ou não na lista
"""

lista = []
cont = ' '

while True:
    lista.append(int(input('Digite um valor: ')))
    while cont not in 'SN':
        cont = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if cont == 'N':
        cont = ' '
        break
    else:
        cont = ' '
print(f'Os {len(lista)} valores digitados, foram {sorted(lista, reverse=True)}')
if 5 not in lista:
    print('O valor 5 não foi digitado.')
else:
    print(f'O valor 5 foi digitado na(s) posição(ões): ', end='')
    for i, v in enumerate(sorted(lista, reverse=True)):
        print(f'{i + 1}... ' if v == 5 else '',end='')
