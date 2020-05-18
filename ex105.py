'''
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário
com as seguintes informações:
    - Quantidade de notas
    - A maior nota
    - A menor nota
    - A média da turma
    - A situação (opcional)
Adicione tb as docstrings da função.
'''


def notas(*nts, mostrasitu=False):
    """
    => Função para analisar notas e situação de uma turma com vários alunos.
    :param nts: uma ou mais notas dos alunos
    :param mostrasitu: parametro opcional, indicando se deve ou não adicionar a situação na saída
    :return: dicionário com informações sobre a turma (quantidade de notas, maior nota, menor nota, média da turma e
    situação (opcional))
    """


    dici = {}
    somants = 0
    dici['qtd'] = len(nts)
    for k, v in enumerate(nts):
        if k == 0:
            dici['maior'] = dici['menor'] = v
        if v > dici['maior']:
            dici['maior'] = v
        if v < dici['menor']:
            dici['menor'] = v
        somants += v

    dici['media'] = somants / dici['qtd']

    if mostrasitu:
        if dici['media'] >= 7:
            dici['situ'] = 'BOA'
        elif dici['media'] >= 5:
            dici['situ'] = 'RAZOÁVEL'
        else:
            dici['situ'] = 'RUIM'

    return dici
'''
    if not mostrasitu:
        return dici['qtd'], dici['maior'], dici['menor'], dici['media']
    if mostrasitu:
        return dici['qtd'], dici['maior'], dici['menor'], dici['media'], dici['situ']
'''

dicionario = notas(3.5, 2, 6.5, 2, 7, 4, mostrasitu=True)
print(dicionario)
