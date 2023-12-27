temp = dict()
dado = list()
gols = list()
print('-' * 36)

#? Inserindo os jogadores
while True:
    nome = str(input('Nome do jogador: ')).strip().capitalize()
    jogos = int(input('partidas jogadas: '))
    for c in range(1, jogos + 1):
        gols.append(int(input(f'Quantos gols na partida {c}: ')))
    temp = {'nome': nome, 'gols': gols[:], 'total': sum(gols)}
    gols.clear()
    dado.append(temp.copy())

    conf = str(input('Deseja continuar? ')).strip().upper()[0]
    if conf == 'N':
        print('-=' * 18)
        break
    else:
        print('-' * 36)

#? Tabela dos jogadores cadastrados
print(f'{"Nº":<3} {"Nome":<15} {"Gols":<10} {"Total":<2}')
print('-' * 36)
for enu, i in enumerate(dado):
    print(f'{enu} {i["nome"]} {i["gols"]} {i["total"]}')

#? Detalhamento do aproveitamento dos jogadores
while True:
    cont = 1
    n = int(input('Exibir dados de qual jogador? (-1 interrompe) '))
    if n == -1:
        break
    print(f'-- LEVANTAMENTO DO JOGADOR {dado[n]["nome"]}')
    for enu, c in enumerate(dado[n]):
        print(c[enu])