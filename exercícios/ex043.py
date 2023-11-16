peso = float(input('Insira seu peso em Kg: '))
altura = float(input('Insira sua altura em metros: '))

imc = peso / altura ** 2
print(f'Seu indíce de masa corporia é {imc:.2f}')


if imc < 18.5:
    print('Você está abaixo do peso') 

elif imc >= 18.5 and imc <= 25:
    print('Seu peso é o ideal')

elif imc > 25 and imc <= 30:
    print('Você está sobrepeso')


elif imc > 30 and imc <= 40:
    print('Obesidade')

else:
    print('Mórbida')