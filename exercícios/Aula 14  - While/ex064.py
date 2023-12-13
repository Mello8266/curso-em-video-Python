# Tratando valores
print('Insira valores e o programa irá soma-los!')
print('Para parar digite 999')
n = cont = 0
while n <= 999:
    n += int(input('n: '))
    cont += 1
n -= 999
print(f'Soma dos valores digitados: {n}')