'''a CBDA precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria
 - <= 9 anos MIRIM
 - <= 14 anos INFANTIL
 - <= 19 anos JUNIOR
 - <= 20 anos SENIOR
 - > 20 anos MASTER'''
# importar bibliotecas para capturar ano atual
from datetime import date

# ler ano de nascimento, calcular e exibir idade
nasc = int(input('Ano de nascimento do atleta: '))
idade = date.today().year - nasc

print('Idade do Atleta: {} anos'.format(idade))

# define categoria
print('Categoria: ', end='')
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JÚNIOR')
elif idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')
