# acrescimo percentual
def aumentar(valor, taxa):
    """
    -> Recebe dois parametros, valor e taxa, e calcula um acrescimo de valor.
    :param valor: valor q vai receber o acrescimo
    :param taxa: taxa de acréscimo em %
    :return: valor com acrescimo de taxa
    """

    return valor * (1 + (taxa / 100))


# desconto percentual
def diminuir(valor, taxa):
    """
    -> Recebe dois parâmetros, valor e taxa, e calcula um desconto de valor.
    :param valor: valor que vai receber o desconto
    :param taxa: taxa de desconto em %
    :return: valor com desconto de taxa
    """

    return valor * (1 - (taxa / 100))


# dobra
def dobra(valor):
    """
    -> Calcula o dobro de um valor.
    :param valor: valor a ser dobrado
    :return: o dobro do valor recebido
    """

    return valor * 2


# metade
def metade(valor):
    """
    -> Calcula a metade de um valor.
    :param valor: valor a ser reduzido pela metade
    :return: a metade do valor recebido
    """

    return valor / 2
