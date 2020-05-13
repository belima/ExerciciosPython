"""
leia uma expressão qualquer que use (parenteses).
analise se a expressão está com os parenteses abertos e fechados na ordem correta.
"""
parenteses = 0
ordemcerta = True

expr = input('Digite uma expressão matemática: ')

for i in expr:
    if i == '(':
        parenteses += 1
    elif i == ')':
        parenteses -= 1
    if parenteses < 0:
        print('Expressão inválida!')
        ordemcerta = False
        break
if ordemcerta == True:
    if parenteses == 0:
        print('Expressão válida!')
    else:
        print('Expressão inválida!')
