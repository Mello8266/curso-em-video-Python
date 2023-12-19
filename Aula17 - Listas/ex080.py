numeros = list()
maior = 0
for c in range(0, 5):
    valor = int(input('Insira um valor: '))
    if c == 0 or valor > maior:
        print(f'Valor adicionado na última posição.')
        numeros.append(valor)
        maior = valor
    else:
        for cont, n in enumerate(numeros):
            if valor < n:
                numeros.insert(cont, valor)
                print(f'Valor adicionado na posição {cont}.')
                break
print(numeros)
        