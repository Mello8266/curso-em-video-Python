# Exercício 107
def metade(n, forma=False):
    if forma:
        f = n / 2
        return formatado(f) #! Ex 109
    else:
        return n / 2

# Exercício 107
def dobro(n, forma=False):
    if forma:
        f = n * 2
        return formatado(f) #! Ex 109
    else:
        return n * 2

# Exercício 107
def aumentar(n, p, forma=False):
    res = n + (n * p / 100)
    if forma:
        return formatado(res) #! Ex 109
    else:
        return res
    
# Exercício 107
def diminuir(n, p, forma=False):
    res = n - (n * p / 100)
    if forma:
        return formatado(res) #! Ex 109
    else:
        return res

#* Exercício 108
def moeda(n):
    return f'R${n:.2f}'

#! Exercício 109
def formatado(n):
    f = f'{n:.2f}'
    formatado = str(f).replace('.', ',')
    return f'R${formatado}'

#? Exercício 110 
def resumo(n, a, d):
    print('-' * 30)
    print(f'{"Resumo do valor":^30}')
    print('-' * 30)

    print(f'{"Preço analisado: ":<20} {formatado(n):>9}')
    print(f'{"Dobro do preço: ":<20} {dobro(n, True):>9}')
    print(f'{"Metade do preço: ":<20} {metade(n, True):>9}')
    print(f'{a}{"% de aumento: ":<18} {aumentar(n, a, True):>9}')
    print(f'{d}{"% de redução: ":<18} {diminuir(n, d, True):>9}')
    print('-' * 30)