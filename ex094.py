'''
leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários
em uma lista. No final, mostre:
    a) quantas pessoas foram cadastradas
    b) a média de idade do grupo
    c) Uma lista com todas as mulheres
    d) uma lista com todas as pessoas com idade acima da média.
'''

pessoa = {}
grupo = []
continua = ' '
somaidade = 0
while True:
    pessoa['nome'] = str(input('Nome > ')).strip().capitalize()
    pessoa['sexo'] = ' '
    while pessoa['sexo'] not in 'MF':
        pessoa['sexo'] = str(input('Sexo [M/F] > ')).strip().upper()[0]
    pessoa['idade'] = 0
    while pessoa['idade'] <= 0:
        pessoa['idade'] = int(input('Idade > '))
    somaidade += pessoa['idade']
    while continua not in 'SN':
        continua = str(input("Continua? [S/N] > ")).strip().upper()[0]
    if continua == 'N':
        continua = ' '
        grupo.append(pessoa.copy())
        break
    elif continua == 'S':
        continua = ' '
        grupo.append(pessoa.copy())

media = somaidade / len(grupo)


print("~~" * 30)
print(f"A) Ao todo temos {len(grupo)} pessoas cadastradas.")
print(f"B) A média de idade é de {media:.2f} anos.")
print("C) As mulheres cadastradas foram:")
for c in range(0, len(grupo)):
    if grupo[c]['sexo'] == 'F':
        print(f"  - {grupo[c]['nome']}")
print("D) Pessoas com idade acima da média registrada:")
for c in range(0, len(grupo)):
    for k, v in grupo[c].items():
        if grupo[c]['idade'] > media:
            if k == 'nome':
                print("    ", end='')
            print(f"{k} = {v}; ", end='')
    if grupo[c]['idade'] > media:
        print()

print("~~" * 30)
print(f"{'<< Encerrado >>':^60}")
