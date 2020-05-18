'''
crie um programa que tenha a função leiaint(), que vai funcionar como um input(), porém aceitando apenas valores
numéricos inteiros.
'''
def leiaint(perg=None):
    while True:
        print(perg, end='')
        inteiro = input().strip()
        if inteiro.isnumeric():
            break
        print('\033[31mApenas números inteiros são aceitos.\033[m')

    return int(inteiro)


n = leiaint('Digite um número: ')
print(f"Você digitou o número {n}")
