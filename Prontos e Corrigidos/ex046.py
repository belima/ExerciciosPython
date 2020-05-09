''' Contagem regressiva de 10 segundos para o estouro de fogos de artifício'''
from time import sleep

for c in range(10, -1, -1):
    sleep(1)
    print('{}!!'.format(c))
print('Feliz ano novooo!!')