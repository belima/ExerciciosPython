print('\n==|Calcula Preço Final|==\n')

preço = float(input('Digite o preço do produto: '))

print('O preço original é {:.2f}.\nO valor para pagamento à vista é {:.2f}.\nO valor para pagamento parcelado é {:.2f}.'.format(preço, preço - (preço*0.1), preço + (preço*0.08)))
