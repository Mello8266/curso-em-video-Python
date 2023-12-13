num = int(input('Insira um número e veja sua tabuada: '))
mult = int(input('Até que número deseja multipiclar? '))

print('-=-' * 5)
for c in range(1, mult+1):
    resultado = num * c
    print(f'{num} x {c:2} = {resultado}')
print('-=-' * 5)