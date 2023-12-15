peso = float(input('Insira seu peso em Kg: '))
altura = float(input('Insira sua altura em metros: '))

imc = peso / (altura ** 2)
print(f'Seu indíce de masa corporia é {imc:.2f}')


if imc < 18.5:
    print('Você está abaixo do peso') 

elif 18.5 <= imc < 25:
    print('Seu peso é o ideal')

elif 25 <= imc < 30:
    print('Você está sobrepeso')


elif 30 <= imc < 40:
    print('Obesidade')

else:
    print('Mórbida')