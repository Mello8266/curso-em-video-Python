matriz = list()
col = list()
cont = indice = c = 0
while indice <= 2:
    col.append(int(input(f'Digite um valor para [{indice}, {cont}]: ')))
    cont += 1
    if cont == 3:
        indice += 1
        matriz.append(col[:])
        col.clear()
        cont -= cont
for n in matriz:
    for i in n:
        if c == 3 or c == 6 or c == 9:
            print('')
        print(f'[{i:^5}]', end='')
        c += 1