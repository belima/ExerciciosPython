'''Faça um programa que leia o ano de nascimento de um jovem e informe:
 - se ainda vai ter q se alistar
 - se é a hora de se alistar
 - se já passou da hora de alistar
  seu prog tb deve mostrar o tempo q falta ou q passou do prazo'''
from datetime import date
# lê ano de nascimento e faz os primeiros cálculos:
nasc = int(input('Digite o ano do seu nascimento: '))
atual = date.today().year
idade = atual - nasc
dif = abs(idade - 18)
print('Quem nasceu em {} tem \033[1;31m{}\033[m anos em {}.'.format(nasc, idade, atual))
# testa idade de alistamento
if idade > 18:
    # testa singular ou plural
    if dif > 1:
        print('Você deveria ter se alistado {} anos atrás, em {}!'.format(dif, atual - dif))
    elif dif == 1:
        print('Você deveria ter se alistado 1 ano atrás, em {}!'.format(atual - dif))
elif idade == 18:
    print('Você deve se alistar esse ano ({})!'.format(atual))
elif idade < 18:
    if dif > 1:
        print('Você deverá se alistar daqui a {} anos!, em {}.'.format(dif, atual + dif))
    elif dif == 1:
        print('Você deverá se alistar daqui a 1 ano, em {}'.format(atual + dif))
