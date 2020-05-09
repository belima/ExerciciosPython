print('\n==|Quantos US$?|==\n')

real = float(input('Quanto dinheiro vc tem? R$'))
cot = 3.27
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, real/cot))
