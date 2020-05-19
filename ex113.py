'''
reescreva a função leiaInt(), do ex104, incluindo agora a possibilidade da digitação de um número de tipo inválido.
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade. Tratar tb a interrupção pelo usuário.
'''


def leiaint(msg=''):

    while True:
        try:
            inteiro = int(input(msg).strip())
        except (ValueError, TypeError):
            print("\033[31mVocê digitou um tipo inválido.\033[m Digite um número inteiro.")
            continue
        except KeyboardInterrupt:
            print("\033[31mO usuário não digitou um valor.\033[m")
            return 0
        except Exception as erro:
            print(f"\033[31mExceção não tratada.")
            print(erro.__class__   )
            continue
        else:
            break
    return inteiro


def leiafloat(msg=''):
    
    while True:
        try:
            flo = float(input(msg).strip().replace(',', '.'))
        except (ValueError, TypeError):
            print('\033[31mVocê digitou um tipo inválido.\033[m Digite um número real.')
            continue
        except (KeyboardInterrupt):
            print("\033[31mExecução interrompida pelo usuário.\033[m")
            return 0
        except Exception as erro:
            print(f"\033[31mExceção não tratada.\033[m")
            print(erro.__class__)
            continue
        else:
            break
    return flo


i = leiaint('digite o int > ')
f = leiafloat('digite o float > ')

print(i, f)
