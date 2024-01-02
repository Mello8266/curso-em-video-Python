from random import randint
numeros = list()

def sortear(lista):
    for c in range(0, 5):
        n = randint(1, 5)
        lista.append(n)
    return numeros

def somaPar(lista):
    soma = 0
    for n in numeros:
        if n % 2 == 0:
            soma += n
    return soma

print('Valores sorteados: ', end='')
for c in sortear(numeros):
    print(c, end=' ')
print(f'\nSoma dos valores pares: {somaPar(numeros)}')