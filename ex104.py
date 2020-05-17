'''
crie um programa que tenha a função leiaint(), que vai funcionar como um input(), porém aceitando apenas valores
numéricos inteiros.
'''
def leiaint(perg=None):
    while True:
        print(perg, end='')
        inteiro = input()
        if inteiro.isnumeric():
            break
        print('Apenas números inteiros são aceitos.')

    return int(inteiro)


a = leiaint('Valor A: ')
b = leiaint('Valor B: ')

s = a + b
print(s)