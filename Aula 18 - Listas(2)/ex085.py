numero = list()
impar = list()
par = list()

for i in range(0, 7):
    num = int(input('Insira um número: '))
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
impar.sort()
par.sort()
numero.append(par[:])
numero.append(impar[:])
print(f'Você digitou os números: {numero}')
