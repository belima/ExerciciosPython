'''
crie uma matriz 3x3 com valores lidos pelo teclado
mostre a matriz formatada corretamente
'''

matriz = []
linha = []

for c in range(0, 3):
    for i in range(0,3):
        linha.append(int(input(f'Digite o valor da posição [{c}, {i}] > ')))
    matriz.append(linha[:])
    linha.clear()

print('~~' * 30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[ {matriz[l][c]:^5} ]', end='')
    print()
