a = float(input('Insira a primeira medida: '))
b = float(input('Insira a segunda medida: '))
c = float(input('Insira a terceira medida: '))



if a + b > c or b + c > a or c + a > b:
    print('Com essas medidas é possível formar um triângulo.')

else:
    print('Com essas medidas é impossível formar um triângulo.')