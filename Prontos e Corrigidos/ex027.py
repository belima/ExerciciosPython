'''Faça um programa que leia o nome completo de uma pessoa e mostre apenas o primeiro e o último nomes, separadamente
Ex.: Ana Maria de Souza
primeiro nome = Ana
ùltimo nome = Souza
'''

nome = str(input('Digite seu nome completo: ')).strip().split()

print('Primeiro nome: {}'.format(nome[0]))
print('Último nome: {}'.format(nome[-1]))
