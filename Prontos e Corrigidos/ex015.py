print('\n==|Aluguel de Carro|==\n')

dias = int(input('Por quantos dias o carro foi alugado? '))
dist = float(input('Qual a distância total percorrida, em km? '))
custodia = 60
custokm = 0.15

print('O valor a pagar é R${:.2f}.'.format(custodia * dias + custokm * dist))
