'''
leia um número e mostre seu fatorial.
'''
n = 1

while n != 0:
        n = int(input('Digite um número para calcular seu fatorial (0 para sair) >'))
        cont = n - 1
        fat = n

        if n != 0:
            while cont > 0:
                fat *= cont
                cont -= 1
            print('{}! = {}'.format(n, fat))
        else:
            print('Nóis')