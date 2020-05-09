'''leia seis numeros inteiros e mostre a soma dos que são pares'''

soma = 0

for c in range(1, 7):
    n = int(input('Digite o {}º número inteiro > '.format(c)))
    if n % 2 == 0:
        soma += n
print('A soma dos pares digitados é {}'.format(soma))
