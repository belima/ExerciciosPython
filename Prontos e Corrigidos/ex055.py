'''leia o peso de 5 pessoas e mostre o maior e o menor.'''


for i in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(i)))

    if i == 1:
        menor = peso
        maior = peso
    else:
        if peso < menor:
            menor = peso
        if peso > maior:
            maior = peso

print('O maior peso digitado foi {:.1f} Kg, e o menor foi {} Kg'.format(maior, menor))
