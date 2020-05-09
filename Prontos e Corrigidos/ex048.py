'''soma de todos os ímpares multiplos de 3 entre 1 e 500'''

soma = 0
cont = 0

for c in range(1, 499, 2):
    if (c % 3 == 0):
        cont += 1
        soma += c
print('A soma dos \033[1;32m{}\033[m valores solicitados é \033[1;33m{}\033[m.'.format(cont, soma))
