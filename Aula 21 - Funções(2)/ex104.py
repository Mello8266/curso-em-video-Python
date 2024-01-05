def leiaInt(txt):
    n = input(f'{txt}')
    if n.isnumeric():
        n = int(n) 
    else: 
        while True:
            print('ERROR! Digite um número inteiro.')
            n = input(f'{txt}')
            if n.isnumeric():
                n = int(n) 
                break
    return n
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número: {n}, somando com ele mesmo: {n + n}')