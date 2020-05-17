'''
faça um programa que tem uma função chamada area(), que receba as dimensões de um terreno retangular (largura e
comprimento) e mostre a área do terreno
'''

def area(l, c):
    a = l * c
    print(f"A área de um terreno {l} x {c} é de {a} m².")


print("Controle de Terrenos")
print("-" * 20)

area(float(input('LARGURA (M) > ')), float(input('COMPRIMENTO (m) > ')))
