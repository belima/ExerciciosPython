'''
leia nome e duas notas de varios alunos e guarde tudo em uma lista composta.
mostre um boletim contendo a média de cada aluno e permita que o usuário possa mostrar
as notas de cada aluno individualmente
'''

from time import sleep

boletim = []
tempaluno = []
tempnotas = []
continua = ' '
nota = -1
chamada = 0

while True:
    aluno = str(input('Nome > ')).strip().title()
    primnome = aluno.split()[0]
    tempaluno.append(aluno[:])
    tempaluno.append(primnome)
    for b in range(1,3):
        while nota < 0 or nota > 10:
            nota = float(input(f'Nota {b} > '))
        tempnotas.append(nota)
        nota = -1
    tempnotas.append((tempnotas[len(tempnotas)-2]+tempnotas[len(tempnotas)-1]) / 2)
    tempaluno.append(tempnotas[:])
    tempnotas.clear()
    boletim.append(tempaluno[:])
    tempaluno.clear()
    while continua not in 'SN':
        continua = str(input('Inserir mais alunos? [S/N] > ')).strip().upper()[0]
    if continua == 'N':
        continua = ' '
        break
    if continua == 'S':
        continua = ' '

print('~~' * 30)
print('Nº  NOME                 MÉDIA')
print('-' * 30)
for i in range(1, len(boletim) + 1):  #todo exibir abrev. do segundo nome caso exista o prim repetido
    print(f'{i}   {boletim[i -1][1]:<22} {boletim[i -1][2][2]:.1f}')
print('-' * 30)

while chamada != 999:
    while chamada not in range(1, len(boletim) + 1) and chamada != 999:
        chamada = int(input('Digite o número do aluno para ver as notas [999 p/ sair] > '))
    if chamada != 999:
        print(f'As notas de {boletim[chamada - 1][0]} foram {boletim[chamada - 1][2][0]} e '
              f'{boletim[chamada - 1][2][1]}.')
        print('~~' * 30)
        chamada = 0
print('encerrando...')
sleep(1)
print('Até a próxima =)')
