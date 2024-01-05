cor = {'limpa':'\033[m',
        'branco': '\033[30m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'amarelo':'\033[33m',
         'azul': '\033[34m',
         'roxo': '\033[35m',
         'bebe': '\033[36m',
         'cinza': '\033[37m'}

def ajuda(txt):
    t = f'Acessando o manual {txt}'
    s = 'SISTEMA DE AJUDA'

    print(f'{cor["azul"]}-' * len(s) * 4)
    print(f'{s}')
    print('-' * len(t) * 4)

    print(f'{cor["verde"]}-' * len(t) * 4)
    print(t)
    print('-' * len(t) * 4)
    print(f'{cor["limpa"]}{help(txt)}')
    

while True:
    resp = str(input('Função ou biblioteca: ')).strip().lower()
    if resp == 'fim':
        break
    ajuda(resp)