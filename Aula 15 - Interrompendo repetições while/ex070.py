cont = s = maior = 0

print('=-=' * 15)
print(f'{"LOJA DO SEU PAI":^45}')
print('=-=' * 15)

while True:
    nome = str(input('Nome do produto: ')).strip().title()
    preco = float(input('Preço do produto: R$'))
    s += preco
    cont += 1

    if cont == 1 or preco < menor:
        pinto = nome
        menor = preco
    if preco > 1000:
        maior += 1
    print('=-=' * 15)

    conf = ''
    while conf not in ('s', 'n'):
        conf = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
    print('-' * 45)  
    print('')   

    if conf in ('n'):
        break
print(f'''Total da compra R${s:.2f}
{maior} produtos acima de R$1000
O produto mais barato é: {pinto} que custa R${menor:.2f}''')