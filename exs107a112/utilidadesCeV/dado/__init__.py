def leiadin(msg):
    """
    -> Validação de dados para valores financeiros. Aceita '.' ou ',' como separador decimal e retorna o valor, float
    com '.'. Não aceita strings vazias ou com letras.
    :param msg: msg a ser apresentada para o usuário
    :return: valor float
    """

    tdnum = True  # inicia uma variavel para checar se todos os caracteres da string são todos numeros ou '.'.
    pts = 0      # inicia uma variavel para checar se há mais de um '.' na string
    while True:
        num = str(input(msg)).strip().replace(',', '.')
        if len(num) != 0:  # se a string for vazia pula o teste e exibe erro
            for i in num:
                if i == '.':
                    pts += 1  # conta o número de '.' na string
                if i not in '0123456789.' or pts > 1:  # levanta flag se string tiver caracteres inválidos
                    tdnum = False
            if tdnum:
                break
            tdnum = True  # zera as variáveis de teste para a próxima entrada do usuário
            pts = 0
            print(f"\033[31mERRO: '{num}' não é um preço válido.\033[m")
        else:
            print(f"\033[31mERRO: '{num}' não é um preço válido.\033[m")

    return float(num)
