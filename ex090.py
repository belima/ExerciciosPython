'''
leia nome e media de um aluno, guardando também a situação final em um dicionário.
mostre o conteúdo da estrutura na tela.
'''
aluno = {}
aluno['nome'] = str(input('Nome do aluno: ')).title().strip()
aluno['media'] = float(input(f"Média de {aluno['nome']}: "))
if aluno['media'] >= 7:
    aluno['situ'] = 'Aprovado'
elif aluno['media'] >= 5:
    aluno['situ'] = 'Recuperação'
else:
    aluno['situ'] = 'Reprovado'

print("~~" * 20)
for k, v in aluno.items():
    print(f"  - {k} é igual a {v}")
