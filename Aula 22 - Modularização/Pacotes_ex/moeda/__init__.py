def metade(n):
    return n / 2

def dobro(n):
    return n * 2

def aumentar(n, p):
    porcentagem = (p / 100) + 1.00
    return n * porcentagem

def diminuir(n, p):
    porcentagem = ((p / 100 ) - 1.00) * - 1
    return n * porcentagem

def moeda(n):
    return f'R${n:.2f}'