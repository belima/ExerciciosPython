'''Refaça o ex035 dos triângulos acrescentando o recurso de mostrar
o tipo do triangulo formado:
 - EQUILATERO - 3 lados iguais
 - ISÓSCELES - 2 lados iguais
 - ESCALENO - todos os lados diferentes'''

# lê tamanho dos segmentos
r1 = float(input('Digite o tamanho do primeiro segmento: '))
r2 = float(input('Digite o tamanho do segundo segmento: '))
r3 = float(input('Digite o tamanho do terceiro segmento: '))

# testa condição de existência do triângulo
if abs(r2 - r3) < r1 < r2 + r3:
    print('Os segmentos acima FORMAM um triângulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO.')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO.')
    else:
        print('ISÓSCELES.')
else:
    print('Os segmentos acima NÃO FORMAM um triângulo.')
