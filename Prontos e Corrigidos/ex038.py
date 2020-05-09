'''Escreva um programa que leia dois numeros inteiros e compare-os,
mostrando na tela uma msg:
 - O primeiro valor é maior
 - O segundo valor é maior
 - Os dois são iguais'''
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
if n1 > n2:
    print('O primeiro número ({}) é maior que o segundo ({}).'.format(n1, n2))
elif n1 < n2:
    print('O segundo número ({}) é maior que o primeiro ({}).'.format(n2, n1))
else:
    print('Os dois números são iguais. ({})'.format(n1))
