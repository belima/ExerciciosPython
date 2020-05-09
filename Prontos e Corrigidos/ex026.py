'''Faça um programa que leia uma frase e mostre:
- Quantas vezes aparece a letra "A".
- Em que posição ela aparece pela primeira vez.
- Em que posição ela aparece pela última vez. '''

frase = str(input('Digite uma frase: ')).strip()

print('Na frase "{}", a letra "A" aparece {} vezes.'.format(frase, frase.lower().count('a')))
print('A primeira aparição da letra "A" é na posição {}.'.format((frase.lower().find('a')) + 1))
print('A última aparição da letra "A" é na posição {}.'.format((frase.lower().rfind('a')) + 1))
