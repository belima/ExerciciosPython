from lib.interface import cor


def arqexiste(nomearq):
    try:
        a = open(nomearq, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criaarq(nomearq):
    with open(nomearq, "wt+") as a:
        return


def adiciona(nomearq, nome, idade):
    with open(nomearq, "a") as arquivo:
        arquivo.write(f"{nome};{idade}\n")
        print(f"{cor('azul')}Novo registro de '{nome}' adicionado.{cor()}")


def learq(nomearq):
    with open(nomearq, "rt") as arquivo:
        for linha in arquivo:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f" {dado[0]:<31} {dado[1]:>3} anos")
