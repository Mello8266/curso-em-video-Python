# Caixa eletrônico

cedula1 = cedula10 = cedula20 = cedula50 = 0

print('=' * 45)
print(f'{"BANCO SEU PAI":^45}')
print('=' * 45)

valor = int(input('Insira o valor a ser sacado: R$'))
text = str(valor)
if len(text) >= 3 and valor >= 50:
    while True:
        cedula50 += 1
        valor -= 50
        if valor < 50:
            break
text = str(valor)
if len(text) == 2 and valor >= 20:
    while True:
        cedula20 += 1
        valor -= 20
        if valor < 20:
            break
text = str(valor)
if len(text) == 2 and valor >= 10 and valor < 20:
    while True:
        cedula10 += 1
        valor -= 10
        if valor < 10:
            break
text = str(valor)
if len(text) == 1 and valor >= 1 and valor < 10:
    while True:
        cedula1 += 1
        valor -= 1
        if valor == 0:
            break
if cedula50 > 0:
    print(f'Total de {cedula50} cédulas de R$50')
if cedula20  > 0:
    print(f'Total de {cedula20} cédulas de R$20')
if cedula10 > 0:
    print(f'Total de {cedula10} cédulas de R$10')
if cedula1 > 0:
    print(f'Total de {cedula1} cédulas de R$1')
print('=' * 45)
