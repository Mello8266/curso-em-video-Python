# Tabuada recursiva

while True:
    n = int(input('Insira um valor e veja sua tabuada: '))
    if n <= 0:
        break
    print('-' * 20)
    for i in range(1, 11):
        print(f'{n} x {i:>2} = {n * i}')
    print('-' * 20)
print('FIM')