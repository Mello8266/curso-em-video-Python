from random import randint
cont = 1

jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6),}

for k, v in jogo.items():
    print(f'O {k} tirou {v}')

print('RANKING DE JOGADORES')
for k, c in jogo.items():
    maior = k
    print(f'{cont}º lugar: {maior} com {jogo[maior]}')
    cont += 1
