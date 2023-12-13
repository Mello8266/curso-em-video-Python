import datetime as dt

print('Insira a data de nascimento de 7 pessoas.')

maioridade = 0
menoridade = 0
for c in range(1, 8):
    data = int(input(f'{c}º data: '))
    idade = dt.date.today().year - data
    print('')
    if idade >= 21:
        maioridade += 1
    else:
        menoridade += 1
print(f'''Dessas 7 pessoas:
{maioridade} pessoas tem mais de 21 anos \n{menoridade} pessoas que tem menos de 21 anos''')
