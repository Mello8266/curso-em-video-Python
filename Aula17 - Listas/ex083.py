exp = (str(input('Insira sua expressão: '))).strip().replace('(', ' ( ').replace(')', ' ) ')
cont = 0
validacao = exp.split()
for v in validacao:
    if v in ('()'):
        cont += 1
print('Sua expressão é válida' if cont % 2 == 0 else 'Sua expressão é inválida!')
