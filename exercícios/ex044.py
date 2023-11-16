preco = float(input('Insira o valor da compra: R$'))
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
    parcela = int(input('Quantas parcelas? '))
    preco = preco * 1.20
    parcela2 = preco / parcela
    print(f'Há juros! {parcela} parcelas mensais no custo de R${parcela2:.2f}')

print(f'O produto vai custar R${preco}!')