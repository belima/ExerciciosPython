'''
Escreva um programa q leia um número n, inteiro, e mostre na tela os n primeiros elementos de uma Fibonacci.
'''

n = termos = 1
a1 = 0
a2 = 1
a3 = a1 + a2
while termos != 0:
    termos = int(input('\nQuantos termos da Fibonacci vc quer ver?\n>>> '))
    if termos != 0:
        print('{}, {}, '.format(a1, a2),end='')
        while n <= termos:
            print('{}, '.format(a3),end='')
            a1 = a2
            a2 = a3
            a3 = a1 + a2
            n += 1
        n = 1
        a1 = 0
        a2 = 1
        a3 = a1 + a2
print('Nóis')

