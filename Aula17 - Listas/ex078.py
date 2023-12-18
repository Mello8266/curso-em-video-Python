num = list()
for c in range(0, 5):
    num.append(int(input(f'Insira o {c}º valor: ')))
print(f'Lista: {num}')
print(f'O maior valor digitado: {max(num)} indice: {num.index(max(num))}')
for n in num:
    indice = num.index(max(num))
    print(indice)
print(f'O maior valor digitado: {min(num)} indice: {num.index(min(num))}')