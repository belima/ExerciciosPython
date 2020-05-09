'''leia uma frase e diga se é um palíndromo, desconsiderando os espaços'''

frase = str(input('Digite uma frase: '))
cut = frase.upper().replace(' ','')

print('"{}" ao contrário é "{}".'.format(cut, cut[::-1]))
if cut == cut[::-1]:
    print('Temos um palíndromo!')
else:
    print('A frase não é um palíndromo!' )

'''
inv = ''
for i in range(len(cut) - 1, -1, -1):
    inv += cut[i]

print('"{}" ao contrário é "{}".'.format(cut, inv))
if cut == inv:
    print('"{}" é um palíndromo!'.format(frase))
else:
    print('"{}" não é um palíndromo!'.format(frase))
'''