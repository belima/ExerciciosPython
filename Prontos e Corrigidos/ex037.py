'''Escreva um programa que leia um numero inteiro qualquer e
peça para o usuário escolher qual será a base de conversão:
- 1 para binário
- 2 para octal
- 3 para hexadecimal'''
print('\033[1;31m-=-\033[m' * 3)
print('\033[1;93mMuda Base\033[m')
print('\033[1;31m-=-\033[m' * 3)
num = int(input('Digite um número inteiro (base 10): '))
print('''Selecione a base desejada:
[2] Binário
[8] Octal
[16] Hexadecimal''')
base = int(input('>>> '))
if base == 2:
    print('{} em BINÁRIO é {:b}'.format(num, num))
elif base == 8:
    print('{} em OCTAL é {:o}'.format(num, num))
elif base == 16:
    print('{} em HEXADECIMAL é {:X}'.format(num, num))
else:
    print('\033[1;31mOpção inválida!\033[m')
