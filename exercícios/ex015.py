print('Calcular aluguel de carro')

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))

total = (dias * 60) + (km * 0.15)

print('O total a ser pago é: R${:.2f}'.format(total))
