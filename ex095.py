'''
aprimore o ex093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do
aproveitamento de cada jogador.
'''
from time import sleep

jogadortemp = {}
gols = []
jogadores = []
separa = '~~' * 30
continua = ' '

while True:
    jogadortemp['nome'] = str(input('Nome do Jogador > ')).strip().capitalize()
    npartidas = int(input('Nº de partidas > '))
    for i in range(0, npartidas):
        if i == 0:
            jogadortemp['gtotal'] = i
        gpartida = int(input(f"   Gols na {i+1}ª partida > "))
        jogadortemp['gtotal'] += gpartida
        gols.append(gpartida)
    jogadortemp['gols'] = gols[:]
    t = len(gols)
    for c in range(0, t):
        gols.pop()
    jogadores.append(jogadortemp.copy())

    while continua not in 'SN':
        continua = str(input('Continua? [S/N] > ')).strip().upper()[0]
    if continua == 'N':
        continua = ' '
        break
    elif continua == 'S':
        continua = ' '

print(separa)
print(" ID Nome           Gols p/ part   Total")
print('-' * 40)

for c in range(0, len(jogadores)):
    print(f"{c+1:>3} {jogadores[c]['nome']:<14} {str(jogadores[c]['gols']):<14} {jogadores[c]['gtotal']}")
print('-' * 40)

while True:
    while continua not in range(1, (len(jogadores) + 1)) and continua != 999:
        continua = int(input('Mostrar dados de qual jogador? [999 p/ sair] > '))
        if continua not in range(1, (len(jogadores) + 1)) and continua != 999:
            print(f"    ERRO! Não existe jogador com ID {continua}")
    if continua == 999:
        continua = 0
        break

    print(f" -- LEVANTAMENTO DO JOGADOR {jogadores[continua - 1]['nome']}:")
    for k, v in enumerate(jogadores[continua - 1]['gols']):
        print(f"    No jogo {k+1} fez {v} gols.")
    continua = 0
print("encerrando...")
sleep(1)
print("    << VOLTE SEMPRE! >>  ")
