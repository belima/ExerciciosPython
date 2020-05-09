'''Crie um programa que jogue jokenpo com vc.'''

# importa bibliotecas para aguardar tempo e selecionar aleatoriamente item de uma lista
from time import sleep
from random import choice

jokenpo = ('Pedra', '', 'Tesoura','', '','Papel') # opções em texto
validos = (0, 2, 5) # opções válidas no menu

print('{:=^20}'.format(' JOKENPO '))

# Jogador escolhe pedra, papel ou tesoura
print('''[ 0 ] PEDRA
[ 5 ] PAPEL
[ 2 ] TESOURA''')

jogador = int(input('Qual a sua jogada?\n> '))

if jogador not in validos: # verifica se opção é válida
    exit('Opção Inválida') # encerra o programa e exibe mensagem se a opção for inválida
    # todo Voltar para menu após opção inválida.

print('Pedra, ',end='')
sleep(0.55)
print('papel ',end='')
sleep(0.55)                          # Exibe a brincadeira com o ritmo do jokenpo
print('e tesooooooou',end='')
sleep(0.55)
print('ra!')
sleep(1)

# máquina escolhe pedra, papel ou tesoura
maq = choice([0, 2, 5])

# exibe escolhas
print('-=' * 11)
print('Máquina jogou {}'.format(jokenpo[maq]))
print('Jogador jogou {}'.format(jokenpo[jogador]))
print('-=' * 11)

# compara escolhas
if jogador == maq: # verifica se empatou
    print('EMPATOU!')
elif (jogador == 0 and maq == 2) or (jogador == 2 and maq == 5) or (jogador == 5 and maq == 0): #verifica se jogador venceu
    print('VOCÊ VENCEU!')
else: # se não empatou nem o jogador venceu, a maquina venceu
    print('VOCÊ PERDEU!')
