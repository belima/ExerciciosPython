'''
ajude um jogador da mega sena a criar palpites.
pergunte quantos jogos serão criados e sorteie 6 numeros,sem repetição, entre 1 e 60 para cada jogo.
cadastrando tudo em uma lista composta.
'''
from random import randint
from time import sleep

jogo = []

print('~~' * 20)
print(f'{"PALPITEIRO":^40}')
print('~~' * 20)

no = int(input('Quantos jogos você quer? > '))

print(f'~~~~~~~~~~ SORTEANDO {no} JOGOS ~~~~~~~~~~~\n' if no > 1 else '~~~~~~~~~~ SORTEANDO 1 JOGO ~~~~~~~~~~~\n')
for j in range(0, no):
    while len(jogo) < 6:
        temp = randint(1, 60)
        if temp not in jogo:
            jogo.append(temp)
    sleep(0.6)
    print(f'Jogo {j + 1}: {sorted(jogo)}')
    jogo.clear()
sleep(0.6)
print('\n~~~~~~~~~~~~~~ BOA SORTE! ~~~~~~~~~~~~~~')