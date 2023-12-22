dado = list()
cadastro = list()
cont = menor = maior = 0
while True:
    dado.append(str(input('Insira o nome: ')).strip().capitalize())
    dado.append(float(input('Insira o peso: ')))
    cadastro.append(dado[:])
    cont += 1
    if cont == 1:
        maior = menor = dado[1]
    if menor > dado[1]:
        menor = dado[1]
    if maior < dado[1]:
        maior = dado[1]
    dado.clear()
    conf = str(input('Deseja cadastrar mais pessoas? [S/N] ')).strip().upper()[0]
    if conf in 'N':
        break
print(f'Você cadastrou {cont} pessoas')
print(f'O maior peso foi {maior}Kg. Peso de ', end='')
for c in cadastro:
    if c[1] == maior:
        print(f'[{c[0]}] ', end='')
print(f'\nO menor peso foi {menor}Kg. Peso de ', end='')
for i in cadastro:
    if i[1] == menor:
        print(f'[{i[0]}] ', end='')
