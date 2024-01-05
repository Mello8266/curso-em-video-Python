c = ('\033[m', # 0 limpa
    '\033[1;37;41m', # 1 vermelho
    '\033[1;37;42m', # 2 verde
    '\033[1;37;43m', # 3 amarelo
    '\033[1;37;44m', # 4 azul
    '\033[1;37;45m', # 5 roxo
    '\033[7;30m'     # 6 branco
    )


def ajuda(txt):
    titulo(f'Acessando o manual do \'{txt}\'', 4)
    print(c[6], end='')
    print(f'{help(txt)}')
    print(c[0], end='')

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('-' * tam)
    print(f'  {msg}  ')
    print('-' * tam)
    print(c[0], end='')

while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    resp = str(input('Função ou biblioteca: ')).strip().lower()
    if resp == 'fim':
        break
    ajuda(resp)
titulo('Até logo!', 1)
