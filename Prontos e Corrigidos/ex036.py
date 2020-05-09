'''Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa.
O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar.
Calcule o calor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou o emprestimo é negado.'''
valor_casa = float(input('Qual o valor do imóvel? R$'))
salario = float(input('Qual sua renda mensal? R$'))
tempo = int(input('Em quantos anos você gostaria de pagar? '))
prest = valor_casa / (tempo * 12)
if prest > (salario * 0.3):
    print('Infelizmente seu empréstimo foi \033[1;31mNEGADO\033[m.')
else:
    print('Empréstimo \033[1;32mAPROVADO\033[m! ')
    print('Para pagar R${:.2f} em {} anos a prestação será de R${:.2f}'.format(valor_casa, tempo, prest))
