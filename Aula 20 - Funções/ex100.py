from random import randint
numeros = list()

def sortear():
    for c in range(0, 5):
        n = randint(1, 5)
        numeros.append(n)
    return numeros

def somaPar():
    soma = 0
    for n in numeros:
        if n % 2 == 0:
            soma += n
    return soma

print(f'Valores sorteados: ', end='')
for c in sortear():
    print(c, end=' ')
print(f'\nSoma dos valores pares: {somaPar()}')