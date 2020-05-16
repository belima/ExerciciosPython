'''
faça um programa que tenha uma função chamada contador(), que receba três parâmetros: 'inicio', 'fim', e 'passo' e
exiba a contagem na tela.
Seu programa deve realizar três contagens através da função criada:
    a) de 1 a 10, de 1 em 1
    b) de 10 a 0, de 2 em 2
    c) uma contagem personalizada.
'''
from time import sleep

def separa(n):
    print("~" * n)

def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1

    separa(40)
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}:")

    if inicio < fim:
        fim += 1
        passo = abs(passo)
    elif inicio > fim:
        fim -= 1
        passo = (abs(passo) * -1)

    for c in range(inicio, fim, passo):
        print(f"{c} ", end='')
        sleep(0.2)
    print("FIM!")


contador(1, 10, 1)

contador(10, 0, 2)

separa(40)

print("Agora é sua vez de personalizar a contagem!")
i = int(input("Início > "))
f = int(input("Fim > "))
p = int(input("Passo > "))

contador(i, f, p)