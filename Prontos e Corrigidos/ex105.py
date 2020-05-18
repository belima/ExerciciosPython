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
    dici['qtd'] = len(nts)
    dici['maior'] = max(nts)
    dici['menor'] = min(nts)
    dici['media'] = sum(nts) / len(nts)

    if mostrasitu:
        if dici['media'] >= 7:
            dici['situ'] = 'BOA'
        elif dici['media'] >= 5:
            dici['situ'] = 'RAZOÁVEL'
        else:
            dici['situ'] = 'RUIM'

    return dici


dicionario = notas(9, 10, 5.5, 2.5, 8.5, mostrasitu=True)
print(dicionario)
