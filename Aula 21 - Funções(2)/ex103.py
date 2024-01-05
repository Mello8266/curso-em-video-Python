def ficha(nome, gols):
    if nome == '':
        nome = '<desconhecido>'
    if gols == '':
        gols = '0'
    print(f'Jogador {nome} fez {gols} gol(s) no campeonato')

nome = str(input('Nome do jogador: ')).strip().capitalize()
gols = str(input('Números de gols: ')).strip()
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0  
ficha(nome, gols)