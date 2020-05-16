'''
leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário.
Se a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
'''

from datetime import date

trabalhador = {}

trabalhador['nome'] = str(input('Nome > ')).strip().capitalize()
nasc = int(input('Ano de nascimento > '))
trabalhador['idade'] = date.today().year - nasc
trabalhador['ctps'] = int(input('Carteira de Trabalho [0 não tem] > '))

if trabalhador['ctps'] != 0:
    trabalhador['contratação'] = int(input('Ano de contratação > '))
    trabalhador['salário'] = float(input('Salário > '))
    trabalhador['aposentadoria'] = (trabalhador['contratação'] + 35) - nasc

print('~~' * 20)
for k, v in trabalhador.items():
    print(f"  - {k} tem o valor {v}")