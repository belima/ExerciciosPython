'''
leia nome e preço de vários produtos, perguntando se o usuário deseja continuar a cada produto.
no final mostre:
    a) valor total da compra
    b) qts produtos acima de R$1000
    c) nome do produto mais barato
'''
from time import sleep

linha = '=' * 40
total = acima1000 = preçomaisbaixo = cont = 0
maisbarato = ''

print(linha)
print(f'{"BL DOCES":^40}')
print(linha)

while True:
    produto = str(input('Produto: ')).strip().capitalize()

    preço = -1
    while preço < 0:
        preço = float(input('Preço: R$').replace(',', '.'))
    cont += 1
    total += preço
    if preço > 1000:
        acima1000 += 1
    if cont == 1 or preço < preçomaisbaixo:
        preçomaisbaixo = preço
        maisbarato = produto

    continua = ' '
    while continua not in 'SN':
        continua = str(input('Registrar outro produto? [S/N] ')).strip().upper()[0]
    if continua == 'N':
        break
print(f'{" FIM DOS ITENS ":-^40}')
sleep(1)
print(f'O total da compra é R${total:.2f}')
print(f'{acima1000} produto custa mais de R$1000' if acima1000 == 1
      else f'{acima1000} produtos custam mais de R$1000')
print(f'{maisbarato} é o produto mais barato, custando R${preçomaisbaixo:.2f}')
sleep(1)
print(linha)
print(f'{"PROGRAMA ENCERRADO":^40}')
print(linha)