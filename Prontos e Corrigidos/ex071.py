'''
simule o funcionamento de um caixa eletronico.
pergunte o valor a ser sacado e informe quantas cédulas de cada valor serão entregues.
o caixa possui cedulas de R$50, R$20, R$10 e R$1,00
'''

linha = '=' * 40
print(linha)
print(f'{" BL BANK ":^40}')
print(linha)

valor = int(input('Olá! Quanto você quer sacar hoje?\n>>> R$'))

notasde100 = int(valor // 100)
valor %= 100
notasde50 = int(valor // 50)
valor %= 50
notasde20 = int(valor // 20)
valor %= 20
notasde10 = int(valor // 10)
valor %= 10
if ((valor % 5) % 2) != 0 and valor % 2 == 0:
    notasde5 = 0
    notasde2 = int(valor // 2)
    valor %= 2
else:
    notasde5 = int(valor // 5)
    valor %= 5
    notasde2 = valor

if valor % 2 != 0:
    print('''Valor inválido. Notas disponíveis:
    R$100, R$50, R$20, R$10, R$5 e R$2''')
else:
    if notasde100 > 0:
        print(f'Cédulas de R$100: {notasde100}')
    if notasde50 > 0:
        print(f'Cédulas de R$50: {notasde50}')
    if notasde20 > 0:
        print(f'Cédulas de R$20: {notasde20}')
    if notasde10 > 0:
        print(f'Cédulas de R$10: {notasde10}')
    if notasde5 > 0:
        print(f'Cédulas de R$5: {notasde5}')
    if notasde2 > 0:
        print(f'Cédulas de R$2: {notasde2}')
print(linha)
print('Até a próxima!')
