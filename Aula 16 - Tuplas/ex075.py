tupla = (int(input('Digite um valor: ')),
        int(input('Digite mais um valor: ')),
        int(input('Digite outro valor: ')),
        int(input('Digite o último valor: ')))

print(f'Você digitou os valores: {tupla}')
print(f'O valor 9 foi digitado: {tupla.count(9)} vezes')
print(f'O valor 3 está na {tupla.index(3) + 1} posição' if 3 in tupla else 'O valor 3 não foi digitado.')
print('Os números pares digitados foram: ', end='')
for i in tupla:
    if i % 2 == 0:
        print(f'{i}', end=' ')
