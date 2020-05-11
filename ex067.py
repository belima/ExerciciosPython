'''
mostre a tabuada de vários números, 1 de cada vez, para cada valor digitado.
o programa para qd o número solicitado for negativo.
'''
from time import sleep

print('~' * 20)
print('TABUADA!')
print('~' * 20)

while True:
    num = int(input('Qual tabuada vc quer ver agora?\n[valor negativo p/ fechar]\n>>> '))
    if num < 0:
        break
    print('~' * 20)
    for i in range(0,11):
        print(f'{num} * {i:<2} = {num * i}')
    print('~' * 20)
print('~' * 20)
print('Encerrando TABUADA!...')
sleep(1)
print('Nóis')
