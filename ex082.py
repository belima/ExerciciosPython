"""
leia vários números e coloque em uma lista.
crie duas listas extras, uma com os valores pares e outra com os valores ímpares.
mostre o conteúdo das 3 listas.
"""

lista = []
continua = ' '

while True:
    lista.append(int(input('Digite um valor: ')))

    while continua not in 'SN':
        continua = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if continua == 'N':
        continua = ' '
        break
    else:
        continua = ' '

pares = []
impares = []

for n in lista:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print(f'Os valores digitados foram {lista}')
print(f'Desses, {pares} são pares e {impares} são ímpares.')

