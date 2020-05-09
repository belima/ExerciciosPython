from math import sin, cos, tan
from math import radians

deg = float(input('Digite o ângulo para saber seu Seno, Cosseno e Tangente: '))
rad = radians(deg)
print('Seno = {:.2f}\nCosseno = {:.2f}\nTangente = {:.2f}'.format(sin(rad), cos(rad), tan(rad)))
