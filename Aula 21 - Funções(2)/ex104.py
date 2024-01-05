def leiaInt(txt):
    n = input(f'{txt}')
    if n.isnumeric():
        n = int(n) 
    else: 
        while True:
            print('\033[0;31mERROR! Digite um número inteiro.\033[m')
            n = input(f'{txt}')
            if n.isnumeric():
                n = int(n)
                break
    return n
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número: {n}, somando com ele mesmo: {n + n}')