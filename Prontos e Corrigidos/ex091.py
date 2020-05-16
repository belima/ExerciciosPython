'''
crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário.
Coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
'''
from time import sleep
from random import randint
from operator import itemgetter

jogos = {}
cont = 1

for i in range(1,5):
    jogos[f'jogador{i}'] = randint(1,6)

print('Valores sorteados:')
for k, v in jogos.items():
    sleep(1)
    print(f"{k} tirou {v} no dado.")

jogosord = dict(sorted(jogos.items(), key=itemgetter(1),reverse=True))

print("-=" * 16)
print("  == RANKING DOS JOGADORES ==  ")
for k, v in jogosord.items():
    sleep(1)
    print(f"{cont}º lugar: {k} com {v}.")
    cont += 1
