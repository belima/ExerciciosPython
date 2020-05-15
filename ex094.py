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
somaidade = 0
while True:
    pessoa['nome'] = str(input('Nome > ')).strip().capitalize()
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F] > ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print("ERRO! Digite M ou F .")
    while True:
        pessoa['idade'] = int(input('Idade > '))
        if pessoa['idade'] > 0:
            break
    somaidade += pessoa['idade']
    grupo.append(pessoa.copy())
    while True:
        continua = str(input("Continua? [S/N] > ")).strip().upper()[0]
        if continua in 'SN':
            break
        print("ERRO! Digite S ou N.")
    if continua == 'N':
        break

media = somaidade / len(grupo)

print("~~" * 30)
print(f"A) Ao todo temos {len(grupo)} pessoas cadastradas.")
print(f"B) A média de idade é de {media:.2f} anos.")
print("C) As mulheres cadastradas foram:")
for c in grupo:
    if c['sexo'] == 'F':
        print(f"  - {c['nome']}")
print("D) Pessoas com idade acima da média registrada:")

for c in grupo:
    if c['idade'] > media:
        print("    ", end='|')
        for k, v in c.items():
            print(f"{k} = {v}", end='|')
        print()

print("~~" * 30)
print(f"{'<< Encerrado >>':^60}")
