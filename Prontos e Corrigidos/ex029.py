'''Escreva um programa que leia a velocidade de um carro.
Se a velocidade ultrapassar 80km/h, informe que ele foi multado e o valor da multa,
que custará R$7,00 por km/h excedente'''

velo = int(input('Qual a velocidade do carro? '))

if velo > 80:
    print('Você excedeu o limite de velocidade. O valor da multa é R${:.2f}.'.format((velo - 80) * 7))
else:
    print('Você está dentro do limite de Velocidade. ')
