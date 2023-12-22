
#? Lista compostas
dados = ['Pedro', 25, 'Jorge', 45, 'Maria', 37]
pessoas = list()
ligacao = list()
ligacao.append(dados) # Cria uma ligação entre as listas
pessoas.append(dados[:]) # Cria uma cópia da lista
print(f'Pessoas é uma lista que contém a lista dados: {pessoas}')
pessoas = [['Pedro', 25], ['Jorge', 45], ['Maria', 37]] # Outra forma de declarar uma lista composta 

#? Posicionamento de itens em listas compostas
print(f'Retorna a sublista inteira: {pessoas[1]}')
print(f'Retorna a lista de índice 2 e o item 0 desta lista: {pessoas[2][0]}') 

#? Lista composta com estrutura de repetição
print('Estrutura for: ')
for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos de idade')
