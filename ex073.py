'''
crie uma tupla com os 20 primeiros colocados da tabela do brasileirão na ordem de colocação.
mostre:
 a) apenas os 4 primeiros colocados
 b) os ultimos 4 colocados da tabela
 c) uma lista com os times em ordem alfabética
 d) em que posição na tabela está o time da chape?
'''

brasileirao2019 = ('Flamengo', 'Santos', 'Palmeiras', 'Gremio', 'Athletico Paranaense', 'Sao Paulo', 'Internacional',
                   'Corinthians', 'Fortaleza', 'Goias', 'Bahia', 'Vasco da Gama', 'Atletico MG', 'Fluminense',
                   'Botafogo', 'Ceara', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avai')

separa = '-' * 40

print('Os 5 primeiros colocados:')
print(brasileirao2019[:5])
print(separa)
print('Os 4 últimos colocados:')
print(brasileirao2019[-4:])
print(separa)
print('Os times listados em ordem alfabética:')
print(sorted(brasileirao2019))
print(separa)
print(f'A Chape está na {brasileirao2019.index("Chapecoense") + 1}ª posição')

