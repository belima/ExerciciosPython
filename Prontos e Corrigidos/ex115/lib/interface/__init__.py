def separa(tamanho=42, c='padrao'):
    print(f"{cor(texto=c)}", end='')
    print('-' * tamanho)
    print(f"{cor()}", end='')


def titulo(texto, tam=42, c='padrao'):
    separa(tam, c)
    print(f"{cor(texto=c)}", end="")
    print(str(texto).center(tam))
    separa(tam, c)


def menu(itens):
    titulo('MENU PRINCIPAL')
    c = 1
    for item in itens:
        print(f"{cor('verde')}{c}{cor()} - {cor('azul')}{item}{cor()}")
        c += 1
    separa()
    opc = lemenu(f"{cor('amarelo')}Sua opção: {cor()}")
    return opc


def cor(texto='padrao', fundo='padrao', estilo='padrao'):
    cortxt = {'padrao'  : '',
              'branco'  : '30',
              'vermelho': '31',
              'verde'   : '32',
              'amarelo' : '33',
              'azul'    : '34',
              'roxo'    : '35',
              'ciano'   : '36',
              'cinza'   : '37'}

    corfundo = {'padrao'  : '',
                'branco'  : ';40',
                'vermelho': ';41',
                'verde'   : ';42',
                'amarelo' : ';43',
                'azul'    : ';44',
                'roxo'    : ';45',
                'ciano'   : ';46',
                'cinza'   : ';47'}

    est = {'padrao'     : '0;',
           'negrito'    : '1;',
           'sublinhado' : '4;',
           'negativo'   : '7;'}

    colorido = f"\033[{est[estilo]}{cortxt[texto]}{corfundo[fundo]}m"

    return colorido


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
            print(erro.__class__)
            continue
        else:
            break
    return inteiro


def lemenu(msg=''):
    from time import sleep

    while True:
        try:
            inteiro = int(input(msg).strip())
        except (ValueError, TypeError):
            print("\033[31mOpção inválida")
            sleep(1)
            continue
        except KeyboardInterrupt:
            print("\033[31mO usuário não digitou um valor\033[m")
            sleep(1)
            return 0
        except Exception as erro:
            print(f"\033[31mExceção não tratada")
            print(erro.__class__)
            sleep(1)
            continue
        else:
            break
    return inteiro