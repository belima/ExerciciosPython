'''
Crie um sistema modularizado que perita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
O sistema só vai ter 2 opções:
    - cadastrar uma nova pessoa
    - listar as pessoas cadastradas
'''
from lib.interface import *
from lib.arquivo import *
from time import sleep


arquivo = "dados.txt"

if arqexiste(arquivo):
    print(f"{cor('azul')}Arquivo '{arquivo}' carregado com sucesso.{cor()}")
else:
    criaarq(arquivo)
    print(f"{cor('vermelho')}Arquivo '{arquivo}' não encontrado. {cor('azul')}Criando.{cor()}")

while True:
    opc = menu(['Ver pessoas cadastradas', 'Cadastrar novas pessoas', 'Sair do sistema'])
    if opc == 1:
        titulo('PESSOAS CADASTRADAS')
        learq("dados.txt")
    elif opc == 2:
        titulo('NOVO CADASTRO')
        nome = str(input('Nome: ')).strip().title()
        idade = leiaint('Idade: ')
        adiciona("dados.txt", nome, idade)
    elif opc == 3:
        print("Encerrando", end='')
        sleep(0.3)
        print(".", end='')
        sleep(0.3)
        print(".", end='')
        sleep(0.3)
        print(".")
        break
    else:
        print(f"{cor('vermelho')}Opção inválida{cor()}")
    sleep(1)
sleep(1)
titulo(f"Até logo!", c='verde')