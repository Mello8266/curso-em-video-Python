valor = float(input('Qual o valor da casa? R$'))
sal = float(input('Qual o seu salário? R$'))
tempo = int(input('Irá parcelar em quantos anos? '))

parcela = valor / (tempo * 12)
print(f'A prestação mensal da casa é de R${parcela:.2f}, em {tempo} anos')

min = sal * 0.3
if parcela > min:
    print('Empréstimo negado!')
    print('As parcelas passam do valor de 30% do seu salário')

else:
    print('Empréstimo concedido.')