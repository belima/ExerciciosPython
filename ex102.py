'''
crie um programa que tenha uma função fatorial() que receba dois parametros:
o primeiro é o numero a calcular e o segundo, chamado 'show', é um valor lógico opcional indicando se será ou não
exibido na tela o processo de calculo do fatorial.
'''


def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número
    :param num: o número a ter o fatorial calculado
    :param show: (opcional) Mostrar ou não a conta
    :return: o valor do Fatorial! de n
    """


    fat = 1
    print('~~' * 20)
    for c in range(num, 0, -1):
        fat *= c
        if show == True:
            print(f"{c}*" if c > 1 else f"{c}=", end='')
    return fat

print(fatorial(8, show=True))
