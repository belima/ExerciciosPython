'''Desenvolva uma logica que calcule o IMC de uma pessoa e mostre sua classificação:
 - < 18.5 abaixo do peso
 - 18.5 < 25 peso ideal
 - 25 < 30 sobrepeso
 - 30 < 40 obesidade
 - > 40 obesidade morbida'''

# solicita dados
peso = float(input('Digite seu peso atual (kg): '))
alt = float(input('Digite sua altura aual (m):'))

# calculo IMC
imc = peso / alt ** 2

# interpreta e exibe IMC
print('Seu IMC atual é {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc < 25:
    print('Você está no peso ideal.')
elif imc < 30:
    print('Você está com sobrepeso.')
elif imc < 40:
    print('ATENÇÃO! Você está com obesidade!')
else:
    print('\033[93;41mCUIDADO!\033[m Você está com obesidade mórbida!')
