'''
faça um programa que tenha uma lista chamada 'numeros' e duas funções, 'sorteia()' e 'somaPar()'.
A primeira função vai sortear 5 numeros e colocá-los dentro da lista e a segunda função vai mostrar a soma entre
todos os valores PARES sorteados pela função anterior.
'''
from random import randint
from time import sleep


numeros = []

def sorteia(lista):
    print("Sorteando 5 valores: ", end='')
    sleep(1)
    for i in range(0,5):
        rnd = randint(0, 100)
        sleep(0.3)
        print(f"{rnd} ", end='')
        lista.append(rnd)
    sleep(0.5)
    print("Pronto!")


def somapar(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    sleep(0.5)
    print(f"A soma dos valores pares em {lista} é {soma}.")

sorteia(numeros)

somapar(numeros)

