print('\n==|Quanta Tinta?|==\n')

l = float(input('Qual a largura da parede? '))
h = float(input('Qual a altura da parede? '))
area = h*l

print('Você vai precisar de {}l de tinta, para pintar esta parede de {} m²!'.format(area/2, area))
