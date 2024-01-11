def linha():
    return print('=-' * 25)


def cor(txt):
    cor = {'limpa':'\033[m',
        'branco': '\033[30m',
        'vermelho':'\033[31m',
        'verde':'\033[32m',
        'amarelo':'\033[33m',
        'azul': '\033[34m',
        'roxo': '\033[35m',
        'bebe': '\033[36m',
        'cinza': '\033[37m'}

    return cor[txt]

def titulo(txt):
    linha()
    print(txt.center(50))
    linha()


def menu(lista):
    i = 1
    for c in lista:
        print(f'{cor("verde")}{i} - {cor("azul")}{c}{cor("limpa")}')
        i += 1
    linha()
    escolha = leiaInt(f'Sua opção: {cor("verde")}', end=True)
    print(cor('limpa'))
    return escolha

def leiaInt(msg, end=False):
    if end:
        print
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro! Digite um número válido.\033[m')
            continue
        else:
            return n
