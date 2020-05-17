'''
faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma
mensagem com tamanho adaptável.
ex:
escreva('Olá, Mundo!')

saída:
~~~~~~~~~~~~~
 Olá, Mundo!
~~~~~~~~~~~~~
'''

def escreva(msg):
    print('-' * (len(msg) + 4))
    print(f"| {msg} |")
    print('-' * (len(msg) + 4))

escreva(str(input('Digite a mensagem para formatar: ')))
