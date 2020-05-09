'''leia o ano de nascimento de 7 pessoas e mostre quantas atingiram a maioridade (21 anos) e quantas não'''
from datetime import date

qt = 0
for i in range(1, 8):
    ano = int(input('Ano de nascimento da {}ª pessoa: '.format(i)))
    if date.today().year - ano >= 21:
        qt += 1

print('\n> {} pessoas atingiram a maioridade e {} não'.format(qt, 7 - qt))
