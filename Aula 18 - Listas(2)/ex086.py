matriz = list()
col = list()
cont = indice = 0
while indice <= 2:
    col.append(int(input(f'Digite um valor para [{indice}, {cont}]: ')))
    cont += 1
    if cont == 3:
        indice += 1
        matriz.append(col[:])
        col.clear()
        cont -= cont
for i, c in enumerate(matriz):
    if i <= 3:
        print(f'[{c}]', end=' ')
    elif i <= 6:
        print(f'\n[{c}]', end=' ')
    elif i <= 9:
        print(f'\n[{c}]', end=' ')