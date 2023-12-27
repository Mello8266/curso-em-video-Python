nome = str(input('Nome do jogador: ')).strip().capitalize()
jogo = int(input('Quanta partidas ele jogou? '))
gols = list()
for c in range(1, jogo + 1):
    gols.append(int(input(f'Quantos gols na partida {c}? ')))
dado = {'nome': nome, 'gols': gols, 'total': sum(gols)}
print('=-' * 20)
for k, v in dado.items():
    print(f'O campo {k} tem o valor {v}')
print('=-' * 20)
print(f'O jogador {dado["nome"]} jogou {jogo} partidas')
for enu, g in enumerate(gols):
    print(f'  => Na partida {enu + 1} ele marcou {g} gols')
print(f'Foi um total de {sum(gols)} gols')
print('=-' * 20)