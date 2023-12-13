cedula1 = cedula10 = cedula20 = cedula50 = 0
valor = int(input('Insira o valor a ser sacado: R$'))
strvalor = str(valor)
while len(strvalor) >= 3:
    valor -= 50
    cedula50 += 1
    if valor == 0:
        break

while len(strvalor) == 2:
    valor -= 50
    cedula20 += 1
    if valor == 0:
        break
print(cedula50, cedula20)