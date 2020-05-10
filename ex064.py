'''
leia vários números inteiros, até q o usuário digite 999.
Mostre quantos números foram digitados e a soma entre eles, desconsiderando o flag (999)
'''
qtd = soma = 0
n = int(input('Digite um número [999 p/ sair]\n> '))

while n != 999:
    qtd += 1
    soma += n
    n = int(input('Mais um [999 p/ sair]\n> '))
if qtd == 1:
    print('Você digitou 1 número, q foi {}.'.format(soma))
else:
    print('Você digitou {} números e a soma entre eles é {}.'.format(qtd, soma))
print('Nóis')
