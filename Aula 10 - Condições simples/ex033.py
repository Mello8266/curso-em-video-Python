n1 = int(input('Insira o primeiro número: '))
n2 = int(input('Insira o segundo número: '))
n3 = int(input('Insira o terceiro número: '))

maior = n1

if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3

print('O maior número é: {}'.format(maior))

menor = n1

if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

print('O menor número é: {}'.format(menor))
