'''
faça um programa que tenha uma função chamada ficha() que receberá dois parâmetros opcionais: o nome de um jogador e
quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador mesmo que algum dado não tenha sido informado corretamente.
'''


def ficha(n='<desconhecido>', g=0):
    return f"O jogador {n} fez {g} gols no campeonato."


print('-' * 20)
nome = str(input('Nome do Jogador: ')).strip().title()
gols = str(input('Número de Gols: '))

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome == '':
    print(ficha(g=gols))
else:
    print(ficha(nome, gols))
