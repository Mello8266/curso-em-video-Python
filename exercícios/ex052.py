print('Insira um número e veja se ele é primo')
n = int(input('número: '))
cont = 0 
for i in range(1, n + 1):
    if n % i == 0:
        print(f'\033[31m {i}', end=' ')
        cont += 1
    else:
        print(f'\033[30m {i}', end=' ')

print(f'\n\033[mO número é divísivel por {cont} números, logo', end=' ')
if cont == 2:
    print(f'{n} é um número primo!')

else:
    print(f'{n} não é primo')