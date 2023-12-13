print('Conversão de temperatura')

graus = float(input('Informe a temperatura em C:'))

kelvin = graus + 273
fah = graus * 9  / 5 +32

print('{}C em Fahrenheit é {}, e em kelvin {}'.format(graus, fah, kelvin))