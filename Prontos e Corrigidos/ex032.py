'''Faça um programa que leia um ano e mostre se é ou não bissexto'''
from datetime import date
print('\n\n-=|Bissexxxto|=-\n')

ano = int(input('Digite um ano para saber se é bissexto: (0 para o ano atual)\n>>> '))

if ano == 0:
    ano = date.today().year

if ((ano % 4 == 0) and (ano % 100 != 0)) or (ano % 400 == 0):
    print('{} é bissexto!'.format(ano))
else:
    print('{} não é bissexto!'.format(ano))
