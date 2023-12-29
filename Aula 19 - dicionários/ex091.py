from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6),}
print('VALORES SORTEADOS: ')
for k, v in jogo.items():
    print(f'O {k} tirou {v}')
    sleep(1)

print('-=' * 15)
ranking = list()
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('RANKING DE JOGADORES')
for i, c in enumerate(ranking):
    print(f'  {i + 1}º lugar: {c[0]} com {c[1]}')
    sleep(1)