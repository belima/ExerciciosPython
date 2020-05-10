'''
leia vários numeros inteiros. O programa deve perguntar se o usuário quer ou não continuar a digitar valores.
mostre a média entre todos os valores e quais foram o maior e menor valores lidos.
'''

n = int(input('Insira um valor: '))
menor = maior = total = n
i = 1

cont = str(input('Deseja inserir mais valores?(S/N) ')).strip().upper()

if cont == 'S':
    while cont == 'S':
        if cont == 'S':
            n = int(input('Insira um valor: '))
            cont = str(input('Deseja inserir mais valores?(S/N) ')).strip().upper()
            total += n
            i += 1
            if n > maior:
                maior = n
            if n < menor:
                menor = n
if i > 1:
    print('A média dos {} valores digitados é {:.2f}.'.format(i, total / i))
    if menor != maior:
        print('O menor valor digitado foi {} e o maior foi {}.'.format(menor, maior))
    else:
        print('Os valores digitados foram iguais.')
else:
    print('O único valor digitado foi {}'.format(n))
