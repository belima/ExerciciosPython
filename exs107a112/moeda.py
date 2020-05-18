def aumentar(valor=0, taxa=0, din=False):
    """
    -> Recebe dois parametros, valor e taxa, e calcula um acrescimo de valor.
    :param valor: valor q vai receber o acrescimo
    :param taxa: taxa de acréscimo em %
    :return: valor com acrescimo de taxa
    """
    ret = valor * (1 + (taxa / 100))

    return moeda(ret) if din else ret


def diminuir(valor=0, taxa=0, din=False):
    """
    -> Recebe dois parâmetros, valor e taxa, e calcula um desconto de valor.
    :param valor: valor que vai receber o desconto
    :param taxa: taxa de desconto em %
    :return: valor com desconto de taxa
    """
    ret = valor * (1 - (taxa / 100))

    return moeda(ret) if din else ret


def dobra(valor=0, din=False):
    """
    -> Calcula o dobro de um valor.
    :param valor: valor a ser dobrado
    :return: o dobro do valor recebido
    """
    ret = valor * 2

    return moeda(ret) if din else ret


def metade(valor=0, din=False):
    """
    -> Calcula a metade de um valor.
    :param valor: valor a ser reduzido pela metade
    :return: a metade do valor recebido
    """
    ret = valor / 2

    return moeda(ret) if din else ret


def moeda(valor=0.0, cur='R$'):
    """
    -> Exibe um valor recebido formatado monetariamente
    :param valor: valor a ser formatado ex: 250.99
    :return: valor formatado ex: R$250,99
    """

    return f"{cur}{valor:.2f}".replace('.', ',')
