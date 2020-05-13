"""
leia diversos valores e armazene em uma lista, não adicionando valores repetidos.
exiba todos os valores únicos digitados, em ordem crescente.
"""

lista = []
continua = ' '

while True:
    valor = int(input('Digite um valor: '))
    if valor not in lista:
        lista.append(valor)
        print('Valor adicionado...')
    else:
        print('Valor já existente. Não adicionado novamente...')

    while continua not in 'SN':
        continua = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if continua == 'N':
        continua = ' '
        break
    else:
        continua = ' '

print('~~' * 20)
print(f'Os valores adicionados, em ordem crescente, são: {sorted(lista)}')
