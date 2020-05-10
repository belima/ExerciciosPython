'''
leia um número e mostre seu fatorial.
'''
# todo Criar versão com for

n = 1

while n != 0:
        n = int(input('Digite um número para calcular seu fatorial (0 para sair) >'))
        cont = n
        fat = 1

        if n != 0:
            print('{}! = '.format(n), end='')
            while cont > 0:
                fat *= cont
                print('{}'.format(cont),end='')
                print(' * ' if cont > 1 else ' = ', end='')
                cont -= 1
            print('{}'.format(fat))
        else:
            print('Nóis')
