'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
Para salários superiores a R$1250,00 calcule um aumento de 10%
Para salários até R$1250,00 calcule um aumento de 15%'''

sal = float(input('Digite o valor do seu salário: R$'))

aumt = 0.1 if sal > 1250 else 0.15

print('Você receberá {}% de aumento (R${:.2f}). Seu novo salário será R${:.2f}'.format(aumt * 100, sal * aumt, sal + sal * aumt))
