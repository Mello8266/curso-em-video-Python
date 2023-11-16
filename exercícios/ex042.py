a = float(input('Insira a primeira medida: '))
b = float(input('Insira a segunda medida: '))
c = float(input('Insira a terceira medida: '))

print('-' * 20)

if a + b > c or b + c > a or c + a > b:
    if a == b == c:
        print('Suas medidas são iguais\nEntão forma se um triângulo equilátero')

    elif a == b or b == c or c == a:
        print('Essas medidas tem dois lados iguais\nEntão forma se um triângulo isóceles')

    else:
        print('Suas medidas são diferentes\nEntão forma se um triângulo escaleno')

else:
    print('Com essas medidas é impossível formar um triângulo.')

print('-' * 20)