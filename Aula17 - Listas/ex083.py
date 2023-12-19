# Inserindo a expressão e dando espaços para cada parêntese
exp = (str(input('Insira sua expressão: '))).strip().replace('(', ' ( ').replace(')', ' ) ')
cont = 0
for p in exp:
    if p in ('()'): # Contando cada parênteses
        cont += 1
print('Sua expressão é válida' if cont % 2 == 0 else 'Sua expressão é inválida!')
