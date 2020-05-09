'''Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas.
- O nome com todas minúsculas.
- Quantas letras tem no total sem considerar espaço.
- Quantas letras tem o primeiro nome.'''

nome = str(input('Digite seu nome completo: ')).strip()

print('Nome em MAIÚSCULAS: {}'.format(nome.upper()))
print('Nome em minúsculas: {}'.format(nome.lower()))
print('Sem contar os espaços, o nome tem {} caracteres.'.format(len(nome) - nome.count(' ')))
print('O primeiro nome tem {} caracteres.'.format(nome.find(' ')))
