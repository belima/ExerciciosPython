from random import sample

a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('Digite o nome do quarto aluno: ')

print('A ordem selecionada para apresentação é:\n{}'.format(sample([a1, a2, a3, a4], 4)))
