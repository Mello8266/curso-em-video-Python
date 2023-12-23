numero = [[], []]
for i in range(0, 7):
    num = int(input('Insira um número: '))
    if num % 2 == 0:
        numero[0].append(num)
    else:
        numero[1].append(num)
numero.sort()
print(f'Os números impares digitados foram: {numero[0]}')
print(f'Os números impares digitados foram: {numero[1]}')