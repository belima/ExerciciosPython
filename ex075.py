'''
leia 4 valores pelo teclado e armazene em uma tupla.
mostre:
 a) quantas vezes apareceu o numero 9
 b) em que posição foi digitado o primeiro valor 3
 c) quais foram os números pares
'''

tupla = (int(input('Valor 1: ')),
         int(input('Valor 2: ')),
         int(input('Valor 3: ')),
         int(input('Valor 4: ')))

print(f'Você digitou os valores: {tupla}')

if 9 in tupla:
    print(f'O número "9" apareceu {tupla.count(9)} vezes.')
else:
    print('O número "9" não foi digitado.')

if 3 in tupla:
    print(f'O primeiro "3" foi digitado na {tupla.index(3) + 1}ª posição.')
else:
    print('Não foi digitado nenhum "3".')

print('Os números pares digitados foram: ')
cont = 0
for n in tupla:
    if n % 2 == 0:
        print(f'- {n}')
        cont += 1
if cont == 0:
    print('- Nenhum número par digitado.')
