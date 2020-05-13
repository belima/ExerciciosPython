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
    nomepeso.append(temp[:])
    temp.clear()

    while continua not in 'SN':
        continua = input('Inserir mais dados? [S/N] > ').strip().upper()[0]
    if continua == 'N':
        continua = ' '
        break
    else:
        continua = ' '

for c in range(0, len(nomepeso)):
    if c == 0:
        menorpeso = maiorpeso = nomepeso[c][1]
    else:
        if nomepeso[c][1] < menorpeso:
            menorpeso = nomepeso[c][1]
        elif nomepeso[c][1] > maiorpeso:
            maiorpeso = nomepeso[c][1]

print('~~' * 30)
print(f'Foi cadastrada 1 pessoa.' if len(nomepeso) == 1 else f'Foram cadastradas {len(nomepeso)} pessoas.')
print(f'Pessoa(s) mais leves, com {menorpeso} Kg: ')
for c in range(0,len(nomepeso)):
    if nomepeso[c][1] == menorpeso:
        print(f'- {nomepeso[c][0]} ')

print(f'Pessoa(s) mais pesadas, com {maiorpeso} Kg: ')
for c in range(0, len(nomepeso)):
    if nomepeso[c][1] == maiorpeso:
        print(f'- {nomepeso[c][0]} ')
