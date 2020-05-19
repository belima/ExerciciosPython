'''
dentro do pacote utilidadesCeV que criamos no ex111, temos um módulo chamado dado. Crie uma função chamada
leiaDinheiro() que seja capaz de funcionar como um input, mas com uma validação de dados para aceitar apenas valores
que sejam monetários. (o programa deve aceitar o uso da virgula como separador decimal)
'''


from utilidadesCeV import dado
from utilidadesCeV import moeda


v = dado.leiadin(msg='Digite o valor > R$')
a = float(input('Quantos % de acréscimo? '))
d = float(input('Quantos % de desconto? '))
moeda.resumo(v, a, d)
