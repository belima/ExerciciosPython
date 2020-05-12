'''
crie uma tupla unica com nomes de produtos e seus respectivos preços, na sequência.
mostre uma listagem de preços, organizando os dados em forma tabular
'''

prodpreços = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99,
              'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9)

linha = '-' * 50

print(linha)
print(f'{"LISTAGEM DE PREÇOS":^50}')
print(linha)

for n in range(0, len(prodpreços), 2):
    print(f'{prodpreços[n]:.<41}R${prodpreços[n+1]:>7.2f}')
print(linha)
