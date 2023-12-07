print('Insira valores e o programa irá soma-los!')
print('Para parar digite 999')
n = 0
while n <= 999:
    n += int(input('n: '))
n -= 999
print(f'Soma dos valores digitados: {n}')