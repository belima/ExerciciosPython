'''
leia idade e sexo de varias pessoas.
a cada pessoa cadastrada, perguntar se deseja continuar inserindo.
no final mostre:
a) qts pessoas tem mais de 18
b) qt homens cadastrados
c) quantas mulheres tem menos de 20 anos
'''

linha = '-' * 30
qtdmaiores = 0
qtdhomens = 0
qtdmulheresabaixo20 = 0

while True:
    print(linha)
    print(f'{"CADASTRE UMA PESSOA":^30}')
    print(linha)

    idade = 0
    while idade <= 0:
        idade = int(input('Idade: '))

    if idade > 18:
        qtdmaiores += 1

    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]

    if sexo == 'M':
        qtdhomens += 1
    elif sexo == 'F' and idade < 20:
        qtdmulheresabaixo20 += 1
    print(linha)

    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N] ').strip().upper()[0])

    if continua == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {qtdmaiores}')
print(f'Ao todo temos {qtdhomens} homem cadastrado' if qtdhomens == 1
          else f'Ao todo temos {qtdhomens} homens cadastrados')
print(f'e {qtdmulheresabaixo20} mulher com menos de 20 anos.' if qtdmulheresabaixo20 == 1
          else f'e {qtdmulheresabaixo20} mulheres com menos de 20 anos.')
