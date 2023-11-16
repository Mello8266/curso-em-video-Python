valor = float(input('Qual o valor da casa? R$'))
sal = float(input('Qual o seu salário? R$'))
tempo = int(input('Irá parcelar em quantos anos? '))

parcela = valor / (tempo * 12)
if parcela > sal / 0.30:
    print('\033[0:31mEmpréstimo negado!')
    print(f'Seu salário R${sal:.2f} não é suficiente para pagar as parcelas {parcela}')

else:
    print(f'Você pagará parcelas de {parcela:.2f} por mês, ao longo de {tempo} anos')