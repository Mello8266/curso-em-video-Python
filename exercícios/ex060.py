n = int(input('Insira um número: '))
cont = 1
resultado = 1

while cont <= n:
    resultado *= cont
    cont += 1
    print(resultado)