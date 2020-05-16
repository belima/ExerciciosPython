'''
aprimore o ex093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do
aproveitamento de cada jogador.
'''
from time import sleep

jogadortemp = {}
gols = []
jogadores = []
separa = '~~' * 30

while True:
    jogadortemp['nome'] = str(input('Nome do Jogador > ')).strip().capitalize()
    npartidas = int(input('Nº de partidas > '))
    gols.clear()
    for i in range(0, npartidas):
        gols.append(int(input(f"   Gols na {i+1}ª partida > ")))
    jogadortemp['gols'] = gols[:]
    jogadortemp['gtotal'] = sum(gols)
    jogadores.append(jogadortemp.copy())

    while True:
        continua = str(input('Continua? [S/N] > ')).strip().upper()[0]
        if continua in 'SN':
            break
        print("ERRO! digite S ou N.")
    if continua == 'N':
        break

print(separa)
print(" ID Nome           Gols p/ part   Total")
print('-' * 40)

for c in range(0, len(jogadores)):
    print(f"{c+1:>3} {jogadores[c]['nome']:<14} {str(jogadores[c]['gols']):<14} {jogadores[c]['gtotal']}")
print('-' * 40)

while True:

    while True:
        busca = int(input('Mostrar dados de qual jogador? [999 p/ sair] > '))
        if busca in range(1, (len(jogadores) + 1)) or busca == 999:
            break
        print(f"    ERRO! Não existe jogador com ID {busca}")
    if busca == 999:
        break

    print(f" -- LEVANTAMENTO DO JOGADOR {jogadores[busca - 1]['nome']}:")
    if len(jogadores[busca - 1]['gols']) == 0:
        print(f"    {jogadores[busca - 1]['nome']} não jogou nenhuma partida.")
    for k, v in enumerate(jogadores[busca - 1]['gols']):
        print(f"    No jogo {k+1} fez {v} gols.")

print("encerrando...")
sleep(1)
print("    << VOLTE SEMPRE! >>  ")
