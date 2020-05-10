'''
leia vários números inteiros, até q o usuário digite 999.
Mostre quantos números foram digitados e a soma entre eles, desconsiderando o flag (999)
'''

n = int(input('Digite um número [999 p/ sair]\n> '))
qtd = 1
soma = n
while n != 999:
    n = int(input('Mais um [999 p/ sair]\n> '))
    if n != 999:
        qtd += 1
        soma += n

if qtd == 1:
    print('Você digitou 1 número, q foi {}.'.format(soma))
else:
    print('Você digitou {} números e a soma entre todos eles é {}.'.format(qtd, soma))
print('Nóis')
