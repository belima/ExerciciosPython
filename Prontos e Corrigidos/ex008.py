tam = float(input('Digite o valor em metros: '))

print('{:.1f}m correspondem a:\n- {:.3f} km\n- {:.2f} hm\n- {:.1f} dam'.format(tam, tam/1000, tam/100, tam/10))
print('- {:.0f} dm\n- {:.0f} cm\n- {:.0f} mm'.format(tam*10, tam*100, tam*1000))
