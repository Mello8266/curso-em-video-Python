num1 = input('Insira um número de 0 a 9999: ')

if len(num1) == 4:
    print('Unidade: {}'.format(num1[3]))
    print('Dezena: {}'.format(num1[2]))
    print('Centena: {}'.format(num1[1]))
    print('Milhar: {}'.format(num1[0]))

elif len(num1) == 3:
    print('Unidade: {}'.format(num1[2]))
    print('Dezena: {}'.format(num1[1]))
    print('Centena: {}'.format(num1[0]))

elif len(num1) == 2:
    print('Unidade: {}'.format(num1[1]))
    print('Dezena: {}'.format(num1[0]))

elif len(num1) == 1:
    print('Unidade: {}'.format(num1[0]))

else:
    print('Insira um número válido')