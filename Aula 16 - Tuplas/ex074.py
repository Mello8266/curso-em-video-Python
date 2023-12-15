from random import randint

tupla = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os números sorteados foram: ', end='')
cont = 0
for c in tupla:
    if cont == 0:
        maior = menor = c
    cont += 1
    if maior > c:
        maior = c
    if menor < c:
        menor = c
    print(c, end=' ')
print(f'\nO menor número sorteado é: {menor} e o maior: {maior}')