# Declarando a lista e inserindo os valores
num = list()
for c in range(0, 5):
    num.append(int(input(f'Insira o {c}º valor: ')))
print(f'Lista: {num}')

# Verificando qual é o maior valor e suas posições
print(f'O maior valor digitado: {max(num)} nas posições: ', end='')
for cont, n in enumerate(num):
    if n == max(num):
        print(f'{cont}...', end=' ')
    
# Verificando qual é o menor valor e suas posições
print(f'\nO maior valor digitado: {min(num)} nas posições: ', end='')
for enu, m in enumerate(num):
    if m == min(num):
        print(f'{enu}...', end=' ')