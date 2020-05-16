'''
faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
seu programa deve analisar todos os valores e dizer qual é o maior.
'''
from time import sleep


def separa():
    print("~~" * 40)


def maior(*n):
    mai = 0
    separa()
    print("Analisando os valores passados... ", end='', flush=True)
    sleep(1)
    for c in n:
        sleep(0.3)
        print(f"{c} ", end='', flush=True)
        if c > mai:
            mai = c
    sleep(0.5)
    print(f"\nForam informados {len(n)} valores.")
    sleep(0.5)
    print(f"O maior valor informado foi {mai}.")


maior(3, 5, 23, 11, 234, 12, 1, 43)
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()