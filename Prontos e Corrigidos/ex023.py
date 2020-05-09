'''Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
Ex.:
Digite um número: 1834

unidade: 4
dezena: 3
centena: 8
milhar: 1
'''

num = int(input('Digite um número entre 0 e 9999: '))
u = num % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000

print('\n{:^14}'.format(num))
print('-' * 14)
print('Unidade(s): {}'.format(u))
print('{:<11} {}'.format('Dezena(s):', d))
print('Centena(s): {}'.format(c))
print('Milhar(es): {}'.format(m))
