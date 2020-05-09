'''leia nome, idade e sexo de 4 pessoas. mostre:
- a média de idade do grupo.
- o nome do homem mais velho
- quantas mulheres tem menos de 20 anos
'''

somaidade = 0
idadehmaisv = 0
qtdmmenos20 = 0
hmaisv = ''
for i in range(1,5):
    print('\n'+'-'* 5, end='')
    print(' {}ª PESSOA '.format(i), end='')
    print('-'* 5)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    gen = str(input('Sexo [M/F]: ')).upper().strip()

    somaidade += idade

    if gen == 'M':
        if idade > idadehmaisv:
            idadehmaisv = idade
            hmaisv = nome

    elif gen == 'F':
        if idade < 20:
            qtdmmenos20 += 1
    else:
        print('\nOpção inválida')


print('\nMédia de idade: {} anos'.format(somaidade / 4))
print('Nome do homem mais velho: {} ({} anos)'.format(hmaisv, idadehmaisv))
print('Nº de mulheres com menos de 20 anos: {}'.format(qtdmmenos20))
