'''Desenvolva um programa que leia o comprimento de 3 retas e diga se elas podem ou não formar um triângulo'''

a = float(input('Comprimento da reta 1: '))
b = float(input('Comprimento da reta 2: '))
c = float(input('Comprimento da reta 3: '))

if (abs(b - c)) < a < b + c:
    print('Você pode formar um triângulo')
else:
    print('Você não pode formar um triângulo')
