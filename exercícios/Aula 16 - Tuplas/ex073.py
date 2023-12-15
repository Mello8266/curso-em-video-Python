classi = ('', 'Palmeiras', 'Grêmio', 'Atlético-MG','Flamengo', 'Botafogo', 'Bragantino', 'Fluminense','Athletico-PR', 'Internacional', 'Fortaleza', 'São Paulo', 'Cuiabá', 'Corinthians', 'Cruzeiro', 'Vasco', 'Bahia', 'Santos', 'Goiás', 'Coritiba', 'América-MG')
print(len(classi))

print('=' * 45)
print('Os cinco primeiros colocados são: ')
for c in range(1, 6):
    print(f'{c}º: {classi[c]}')
print('=' * 45)

print('Os quatro últimos: ')
for i in range(17, 21):
    print(f'{i}º: {classi[i]}')
print('=' * 45)

alfa = sorted(classi)
print('Em ordem alfabética: ')
for a in range(1, 21):
    print(f'{alfa[a]},' if a < 20 else f'{alfa[a]}.', end=' ')
print('')
print('=' * 45)

print('O Santos está na {}º posição'.format(classi.index('Santos')))