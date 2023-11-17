print('Insira seis digitos e o programa irá calcular os números pares digitados e desconsideras os ímpares')

soma = 0
print('-=-' * 20)
for c in range(1, 7):
    num = int(input('Insira os digitos: '))
    if num % 2 == 0:
        soma += num
print('-=-' * 20)
print(f'A soma dos valores pares é: {soma}')