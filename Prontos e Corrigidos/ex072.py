'''
leia um numero de 0 a 20 e retorne o mesmo por extenso, retirado de uma tupla
'''
extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
       'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    alg = int(input('Digite um número entre 0 e 20 > '))

    if 0 <= alg <= 20:
        break
    print('Tente novamente. ',end='')
print(f'Você digitou \033[31m{extenso[alg]}\033[m.')
