'''Calcule um programa que leia 4 notas de um aluno e informe a situação do aluno no final do ano
- reprovado
- recuperação
- aprovado'''

# lê notas do aluno e calcula sua média:
p1 = float(input('\033[30mNota da P1: '))
p2 = float(input('Nota da P2: '))
p3 = float(input('Nota da P3: '))
p4 = float(input('Nota da P4: '))

media = float((p1 + p2 + p3 + p4)/4)

# verifica e informa situação do aluno:
print('Sua média é {}'.format(media))
if media >= 7:
    print('Parabéns! Você está \033[1;34mAPROVADO\033[30m.')
elif 5 <= media < 7:
    print('Você está em \033[1;93mRECUPERAÇÃO\033[30m.')
elif media < 5:
    print('Você está \033[1;31mREPROVADO\033[30m.')
