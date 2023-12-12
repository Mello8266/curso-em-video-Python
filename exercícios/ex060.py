# Cálculo de fatorial
n = int(input('Insira um número: '))
cont = n
resultado = 1
print(f'{n}! = ', end='')

# Utilizando o While
while cont > 0:
    print(f'{cont}', end='')
    print(' x ' if cont > 1 else ' = ', end='')
    resultado *= cont
    cont -= 1
print(resultado)

# Utilizando o for
for n in range(n, 0, -1):
    print(f'{n}', end='')
    print(' x ' if n > 1 else ' = ', end='')
    resultado *= n
print(resultado)