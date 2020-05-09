'''Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra "SANTO". '''

city = str(input('Digite o nome da cidade: ')).strip().lower().split()

print('O nome da cidade começa com "Santo"? {}'.format(city[0] == 'santo'))
