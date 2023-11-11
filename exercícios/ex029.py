v = float(input('Qual a velocidade que o carro foi fotografado? '))
if v > 80:
    multa = (v - 80) * 7
    print('Veículo multado, valor: R${}'.format(multa))

else:
    print('Veículo passou dentro da faixa de velocidade!')