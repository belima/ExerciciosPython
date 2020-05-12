"""
crie uma tupla com várias palavras(não use acentos).
mostre, para cada palavra, quais são suas vogais.
"""

palavras = ('caneca', 'monitor', 'joypad', 'simulador', 'mouse', 'alcool', 'pandemia', 'coronavirus')
vogais = ('a', 'e', 'i', 'o', 'u')

for p in palavras:
    print(f'As vogais em "{p.upper()}" são ', end='')
    for l in p:
        if l in vogais:
            print(l, end=' ')
    print()
