n = int(input('Insira um número: '))
m = (n - 1) + (n - 2)

while m <= n:
    m += (n - 1) + (n - 2)
    print(m)