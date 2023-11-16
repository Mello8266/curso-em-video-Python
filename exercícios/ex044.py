preco = float(input('Insira o valor do produto: '))
print('-' * 20)
print('Formas de pagamento: a vista dinheiro\na vista cartão\n2x no cartão\n3x ou mais no cartão ')
print('-' * 20)
forma = str(input('Qual a forma de pagamento? ')).strip().lower()

if forma == 'dinheiro':
    preco = preco * 0.9 
    

elif forma == '1x':
    preco = preco * 0.95

elif forma == '2x':
    parcela = preco / 2
    print(f'Preço da parcela R${parcela}')

elif forma == '3x':
    preco = preco * 1.20
    print('Há juros!')


print(f'O produto vai custar R${preco}!')