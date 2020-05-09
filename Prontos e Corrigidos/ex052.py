'''leia um numero inteiro e diga se é primo'''

n = int(input('Digite um número inteiro > '))

'''
primo = 1

for c in range(2, n):
    if (n == 1) or (n % c == 0):
        primo = 0

if primo == 0:
    print('{} não é primo!'.format(n))
else:
    print('{} é primo!'.format(n))
'''

tot = 0

for c in range(1, n + 1):
    if n % c == 0:
        print('\033[92m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{}\033[m'.format(c), end=' ')
    if c % 20 ==0:
        print('\n')
print('\n')
if tot == 2:
    print('{} é divisível por 2 números, logo é primo!'.format(n))
else:
    if tot == 1:
        print('{} é divisível por 1 número, logo não é primo!'.format(n))
    else:
        print('{} é divisível por {} números, logo não é primo!'.format(n, tot))
