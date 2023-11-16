dis = float(input('Insira a distância da viagem em km: '))

if dis <= 200:
    preco = dis * 0.50
else:
    preco = dis * 0.45

print(f'O valor da passagem será de: R${preco}')