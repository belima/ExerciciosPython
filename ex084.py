'''
leia nome e peso de várias pessoas, guardando em uma lista.
mostre:
    a) quantas pessoas cadastradas?
    b) uma listagem com as pessoas mais pesadas
    c) uma listagem com as pessoas mais leves
'''

nomepeso = []
temp = []
continua = ' '
menorpeso = maiorpeso = 0

while True:
    temp.append(str(input('Nome > ')).strip().title())
    temp.append(float(input('Peso > ')))
    if len(nomepeso) == 0:
        menorpeso = maiorpeso = temp[1]
    else:
        if temp[1] < menorpeso:
            menorpeso = temp[1]
        elif temp[1] > maiorpeso:
            maiorpeso = temp[1]
    nomepeso.append(temp[:])
    temp.clear()

    while continua not in 'SN':
        continua = input('Inserir mais dados? [S/N] > ').strip().upper()[0]
    if continua == 'N':
        continua = ' '
        break
    else:
        continua = ' '

print('~~' * 30)
print(f'Foi cadastrada 1 pessoa.' if len(nomepeso) == 1 else f'Foram cadastradas {len(nomepeso)} pessoas. ')
print(f'Pessoa(s) mais leves, com {menorpeso} Kg: ')
for c in nomepeso:
    if c[1] == menorpeso:
        print(f'- {c[0]} ')

print(f'Pessoa(s) mais pesadas, com {maiorpeso} Kg: ')
for c in nomepeso:
    if c[1] == maiorpeso:
        print(f'- {c[0]} ')
