from time import sleep
from random import randint

mega = list()
sena = list()

print('-=-' * 15)
print(f'{"Jogo da mega sena":^45}')
print('-=-' * 15)
jogos = int(input('Quanto jogos serão sorteados? '))
cont = 0
while cont <= jogos:
    for c in range(0, 6):
        n = randint(1, 60)
        if n not in sena:
            sena.append(n)
        if len(sena) == 6:
            sena.sort()
            mega.append(sena[:])
            sena.clear()
    cont += 1
print('-=' * 6, f'SORTEANDO {jogos} JOGOS', '-=' * 6)
for enu, i in enumerate(mega):
    print(f'Jogo {enu + 1}: {i}')
    sleep(1.5)