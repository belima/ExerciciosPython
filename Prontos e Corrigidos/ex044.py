'''Elabore um programa que calcule o valor a ser pago por um produto, considerando a forma de pagamento
 - a vista din/cheque: 10% de desconto
 - a vista no cartão: 5% de desc
 - até 2x no cartão: preço normal
 - acima de 2x no cartão: acresc de 20%'''
from sys import exit

print('{:=^40}'.format(' PY LOJAS '))

# solicita valor a ser pago
valor = float(input('Valor a ser pago: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
sel = int(input('Digite a opção desejada\n> '))

# aplica descontos/acréscimos
if sel == 1:
    final = valor * 0.9
    print('Desconto de 10% ({:.2f}) para pagamento à vista no dinheiro/cheque'.format(valor * 0.1))
elif sel == 2:
    final = valor * 0.95
    print('Desconto de 5% ({:.2f}) para pagamento à vista no cartão'.format(valor * 0.05))
elif sel == 3:
    final = valor
    print('2 parcelas de R${:.2f}'.format(final / 2))
elif sel == 4:
    final = valor * 1.2
    n_parcelas = int(input('Digite o número de parcelas\n> '))
    print('Acréscimo de 20% ({:.2f}) para pagamento acima de 3x no cartão'.format(valor * 0.2))
    print('{} parcelas de R${:.2f}'.format(n_parcelas, final / n_parcelas))
else: # termina o programa se a opção for inválida
    print('\033[31mOpção inválida\033[m')
    exit()

# exibe valor final
print('Valor total a ser pago: R${:.2f}'.format(final))
