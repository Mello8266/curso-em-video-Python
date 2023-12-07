n = int(input('Insira m número: '))
n += 1
f = 0
while n > 1:
    n -= 1
    f += n * n
    print(f)