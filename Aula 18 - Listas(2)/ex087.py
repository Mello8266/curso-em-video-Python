matriz = list()
col= list()
cont = indice = c = somap = 0
while indice <= 2:
    n = int(input(f'Insira um valor para [{indice}, {cont}]: '))
    col.append(n)
    if n % 2 == 0:
        somap += n
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
print(f'\nA soma dos números pares: {somap}')
print(f'A soma da terceira coluna é: {matriz[0][2] + matriz[1][2] + matriz[2][2]}')
print(f'O maior valor da segunda linha é: {max(matriz[1])}')
