'''Escreva um programa que pergunte a distância total de uma viagem, em km.
Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km
e R$0,45 para viagens mais longas'''

dist = int(input('Qual a distância total da viagem, em km?\n>>> '))

print('O valor da Passagem é R${:.2f}.'.format((dist * 0.5) if dist <= 200 else (dist * 0.45)))
