numeros = list()
while True:
    numeros.append(int(input('Digite um número: ')))
    conf = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if conf in 'N':
        break
print(f'Você digitou {len(numeros)} valores')
numeros.sort(reverse=True)
print(f'Valores em ordem decrescente: {numeros}')
print('O valor 5 ', end='')
print('está na lista' if 5 in numeros else 'não está na lista')