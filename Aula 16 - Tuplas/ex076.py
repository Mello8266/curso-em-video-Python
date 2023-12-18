setup = ('computador', 2800.00, 'monitor', 600.00, 'teclado', 110.54, 'mouse', 140.43, 'mousepad', 70.81, 'mesa', 178.70)

print('=-=' * 10)
print(f'{"Lista de preços":^30}')
print('=-=' * 10)

for c in setup:
    if type(c) == str:
        print(f'{c:.<20}', end='')
    if type(c) == float:
        print(f'R${c:>8.2f}')
