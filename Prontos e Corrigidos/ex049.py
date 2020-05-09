'''refaça o desafio 9 (tabuada) utilizando 'for' '''

print('\n==!Tabuada!==\n')

n1 = int(input('Digite um número para ver sua tabuada: '))

print('\n=Tabuada de {}='.format(n1))
print('-'*14)
for c in range(1, 11):
    print('- {} x {:2} = {}'.format(n1, c, n1 * c))
print('-'*14)
