'''
Escreva um programa q leia um número n, inteiro, e mostre na tela os n primeiros elementos de uma Fibonacci.
'''

# inicia variáveis
n = termos = 1
a1 = 0      # Os primeiros dois termos de uma fibonacci são 0 e 1.
a2 = 1
a3 = a1 + a2    # Os termos seguintes são a soma dos dois termos anteriores.

# executa enquanto usuário não pressiona 0
while termos != 0:
    termos = int(input('\nQuantos termos da Fibonacci vc quer ver?\n>>> '))
    if termos == 1:
        print('{}'.format(a1),end='')   # Imprime 1 termo
    if termos == 2:
        print('{}, {}'.format(a1, a2),end='')   # Imprime 2 termos
    if termos > 2:
        print('{}, {}'.format(a1, a2),end='')   # Imprime 3 ou mais termos

        while n <= termos -2:
            print(', {}'.format(a3),end='')
            a1 = a2     # Passa os valores de a2 e a3 p/ a1 e a2, respectivamente, para q se calcule a3 = a1 + a2
            a2 = a3
            a3 = a1 + a2    # Calcula o termo atual somando os dois anteriores
            n += 1      # Conta um passo em direção ao número de termos a serem calculados

        n = 1       #reinicia todas as váriáveis para a próxima iteração
        a1 = 0
        a2 = 1
        a3 = a1 + a2
print('Nóis')       # msg de finalização
