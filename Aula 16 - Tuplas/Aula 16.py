# Declarando a tupla
lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
pessoa = ('Vinnycius', 19, 'M', 76.34) # Pode ter diferentes tipos de dados dentro da tupla

# Formas de manipular a tupla
print(f'Print do segundo elemento até o último: {lanche[1:]}')
print(f'Último elemnto da tupla: {lanche[-1]}')
print(f'Número de elementos tupla: {len(lanche)}')
print(f'Tupla ordenada: {sorted(lanche)}')

# "Somar" tuplas
a = (1, 2, 3, 4)
b = (4, 5, 6)
c = a  + b
d = b + a # d != c
print(f'Tupla c: {c} \nTupla d: {d}')
print(c.count(2)) # Printa quantos 2 há na tupla
print(d.index(4, 1)) # Printa a posição do primeiro 4 na tupla procurando a partir do seg. item

# Estrutura de repetição com tupla
print('Primeira forma com for: ')
for c in lanche: # Exibe cada um dos itens na variável c, um item para cada repetição
    print(c)

print('Segunda forma com for enumerando os itens: ')
for posicao, c in enumerate(lanche): # A enumeração é feita na variável posicao
    print(f'{c}, posição do item: {posicao}', end=' ')

print('\nSegundo for: ')
for cont in range(0, len(lanche)): # Repetição que vai do zero até o número de elementos na tupla
    print(f'{lanche[cont]}, item: {cont} -', end=' ')
