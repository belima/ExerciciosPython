'''
faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
peça a digitação novamente até obter um valor válido.
'''
val = ('m', 'M', 'f', 'F')

sex = str(input('Sexo > '))

while sex not in val:
    if sex not in val:
        print('\033[31mOpção inválida\033[m')
        sex = str(input('Sexo > '))

print('\033[32mOpção válida\033[m')
