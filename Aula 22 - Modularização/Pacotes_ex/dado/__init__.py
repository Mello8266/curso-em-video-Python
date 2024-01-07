def leiadinheiro(txt):
    num = 0
    ponto = 0
    while True:
        n = input(f'{txt}')
        if n.isnumeric():
            return float(n)
        else:
            for c in n:
                if c == ',' or c == '.':
                    ponto += 1
                if c.isnumeric():
                    num += 1
            if ponto == 1 and num > 0:
                n = n.replace(',', '.')
                return float(n)    
        print(f'ERRO! "{n}" não é um preço válido.')
