'''
crie um programa que tenha uma função chamada voto(). A função recebe ano de nascimento e retorna a condição
de voto ['NEGADO', 'OPCIONAL ou 'OBRIGATÓRIO'] para as eleições.
ref.: - abaixo de 16 não vota
      - de 16 a 17 ou maior de 65 voto opcional
      - de 18 a 65 voto obrigatório
'''


def voto(nasc):
    """
    Verifica se nascidos em um determinado ano devem ou não votar nas eleições.
    :param nasc: Ano de nascimento.
    :return: Condição de voto [NEGADO, OPCIONAL, OBRIGATÓRIO]
    """

    from datetime import date
    global idade

    idade = int(date.today().year - nasc)

    if idade < 16:
        return "VOTO NEGADO"
    elif idade < 18 or idade > 65:
        return 'VOTO OPCIONAL'
    else:
        return 'VOTO OBRIGATÓRIO'


print('~' * 30)
ano = int(input(' Em que ano você nasceu? '))
situ = voto(ano)
print(f"IDADE: {idade}\n{situ}")