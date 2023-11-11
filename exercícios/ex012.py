preco = float(input('Insira o valor do produto: '))

print('O produto custa R${:.2f}'.format(preco))
print('Com desconto de 5% fica R${:.2f}'.format(preco * 5/100))

#outra maneira
preco = float(input('Insira o valor do produto: '))

print('O produto custa R${:.2f}'.format(preco))
novo = preco - (preco * 5 / 100)

print('Com desconto de 5% fica R${:.2f}'.format(novo))