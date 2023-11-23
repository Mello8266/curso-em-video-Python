print('Insira um número e veja se ele é primo')
n = int(input('número: '))

if n / n == 1 and n % 2 != 0 and n % 3 != 0:
    print(f'{n} é um número primo!')

else:
    print(f'{n} não é primo')