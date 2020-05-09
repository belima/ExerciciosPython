print('\033[1;34m-=-\033[m'*2)
print('\033[1;33mSoma!')
print('\033[1;34m-=-\033[m'*2)

n1 = int(input('\n\nDigite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2

print('A soma entre \033[34m{}\033[m e \033[33m{}\033[m é igual a \033[32m{}\033[m!'.format(n1, n2, s))
