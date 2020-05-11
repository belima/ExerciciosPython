'''
leia varios numeros inteiros. pare qd o usuário digitar 999.
mostre quantos numeros foram digitados e ql a soma entre eles, desconsiderando o flag
'''

cont = soma = 0

while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A soma entre os {cont} números digitados é {soma}.')
