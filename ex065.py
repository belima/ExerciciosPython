'''
leia vários numeros inteiros. O programa deve perguntar se o usuário quer ou não continuar a digitar valores.
mostre a média entre todos os valores e quais foram o maior e menor valores lidos.
'''

n = int(input('Insira um valor: '))
menor = n
maior = n
i = 1
total = n

cont = str(input('Deseja inserir mais valores?(S/N) '))

if cont not in 'nN':
    while cont not in 'nN':
        if cont not in 'nN':
            n = int(input('Insira um valor: '))
            cont = str(input('Deseja inserir mais valores?(S/N) '))
            total += n
            i += 1
            if n > maior:
                maior = n
            if n < menor:
                menor = n
if i > 1:
    print('A média dos {} valores digitados é {:.2f}.'.format(i, total / i))
    print('O menor valor digitado foi {} e o maior {}.'.format(menor, maior))
else:
    print('O único valor digitado foi {}'.format(n))
