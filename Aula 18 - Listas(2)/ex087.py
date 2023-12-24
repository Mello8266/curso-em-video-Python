matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somap = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Insira um número para [{l}][{c}]: '))
        if matriz[l][c] % 2 == 0:
            somap += matriz[l][c]
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f'A soma dos valores pares é {somap}')
print(f'A soma dos valores da terceira coluna é {matriz[0][2] + matriz[1][2] + matriz[2][2]}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')