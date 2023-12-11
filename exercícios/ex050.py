print('Insira seis digitos e o programa irá calcular os números pares digitados e desconsideras os ímpares')

soma = 0
cont = 0
print('-=-' * 10)
for c in range(1, 7):
    num = int(input(f'Insira o {c}º digito: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print('-=-' * 10)
print(f'A soma dos {cont} números pares digitados é: {soma}')