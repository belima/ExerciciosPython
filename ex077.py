'''
crie uma tupla com várias palavras(não use acentos).
mostre, para cada palavra, quais são suas vogais.
'''

palavras = ('caneca', 'monitor', 'joypad', 'simulador', 'mouse', 'alcool', 'pandemia', 'coronavirus')
vogais = ('a', 'e', 'i', 'o', 'u')

for p in range(0, len(palavras)):
    print(f'As vogais em "{palavras[p]}" são ', end='')
    for l in range(0, len(palavras[p])):
        if palavras[p][l] in vogais:
            print(f'{palavras[p][l]} ', end='')
    print()
