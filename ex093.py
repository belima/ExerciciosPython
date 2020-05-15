'''
crie um programa que gerencie o aproveitamento de um jogador de futebol
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada
partida. No final, tudo será guardado em um dicionário, incluindo o total de gols feitos durante o camponato
'''

jogador = {}
gols = []
separa = '~~' * 30

jogador['nome'] = str(input('Nome do Jogador > ')).strip().capitalize()
npartidas = int(input('Nº de partidas > '))
for i in range(0, npartidas):
    if i == 0:
        jogador['gtotal'] = i
    gpartida = int(input(f"   Gols na {i+1}ª partida > "))
    jogador['gtotal'] += gpartida
    gols.append(gpartida)
jogador['gols'] = gols[:]

print(separa)
print(jogador)
print(separa)
for k, v in jogador.items():
    print(f"O campo {k} tem o valor {v}")
print(separa)
print(f"O jogador {jogador['nome']} jogou {npartidas} partidas.")
for i in range(0, npartidas):
    print(f"    => Na partida {i+1}, fez {jogador['gols'][i]} gols.")
print(f"Foi um total de {jogador['gtotal']} gols.")