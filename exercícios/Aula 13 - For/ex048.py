soma = 0
total = 0
print('-=-' * 41)
for c in range (1, 501, 2):
    if c % 3 == 0:
        soma += c
        total += 1
        print(c, end=' ')

print('')
print('-=-' * 41)
print(f'A soma dos {total} valores é {soma}')