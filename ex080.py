"""
leia 5 valores numericos e cadastre-os em uma lista ordenada, já na posição correta de inserção, sem utilizar
sort().
Mostre a lista ordenada.
"""
from time import sleep

lista = []

for c in range(0,5):
    n = int(input('Digite um valor: '))
    if len(lista) == 0:
        lista.append(n)
        print(f'{n} inserido na {len(lista)}ª posição.')
    else:
        for i, v in enumerate(lista):
            if n <= v:
                lista.insert(i, n)
                print(f'{n} inserido na {i + 1}ª posição.')
                break
            else:
                if i == len(lista) - 1:
                    lista.append(n)
                    print(f'{n} inserido na {len(lista)}ª posição.')
                    break
sleep(1)
print(f'Os valores inseridos foram: {lista}')
