from random import randint

tupla = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os números sorteados foram: ', end='')
cont = 0
for c in tupla:
    print(c, end=' ')
print(f'\nO menor número sorteado é {min(tupla)} e o maior é {max(tupla)}')
