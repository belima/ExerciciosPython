'''
aprimore o ex086, mostrando:
    a) a soma dos valores pares digitados
    b) a soma dos valores da terceira coluna
    c) o maior valor da segunda linha
'''

matriz = []
linha = []
somapares = 0
somaterc = 0

for c in range(0, 3):
    for i in range(0,3):
        linha.append(int(input(f'Digite o valor da posição [{c}, {i}] > ')))
    matriz.append(linha[:])
    linha.clear()

print('~~' * 30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[ {matriz[l][c]:^5} ]', end='')
        if matriz[l][c] % 2 == 0:
            somapares += matriz[l][c]
        if c == 2:
            somaterc += matriz[l][c]
    print()
print('~~' * 30)
print(f'A soma dos valores pares é {somapares}.')
print(f'A soma dos valores da terceira coluna é {somaterc}.')
print(f'O maior valor da segunda linha é {max(matriz[1])}.')
