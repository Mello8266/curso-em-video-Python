total = list()
par = list()
impar = list()

while True:
    total.append(int(input('Insira um valor: ')))
    print('Valor adicionado.')
    conf = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if conf in 'N':
        for n in total:
            if n % 2 == 0:
                par.append(n)
            else:
                impar.append(n)
        break
par.sort()
impar.sort()
print(f'você digitou os valores: {total}')
print(f'Valores pares digitados: {par}')
print(f'Valores impares digitados: {impar}')
