num = float(input('Insira um número e veja sua tabuada: '))
mult = int(input('Até que número deseja multipiclar? '))

print('-=-' * 15)
for c in range(1, mult+1):
    resultado = num * c
    print(f'{num} x {c} = {resultado:.2f}')
print('-=-' * 15)