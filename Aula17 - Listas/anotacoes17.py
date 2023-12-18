
#? Forma de declarar lista - []
lista = [] # Declarar lista vazia
lanche = ['hamburguer', 'suco', 'pizza', 'pudim']
valores = list(range(4, 11))
print('-' * 60)
print(f'Lista gerada com range: {valores} há {len(valores)} itens')
print('-' * 60)
type(lanche) # Retorna list

#? Lista pode ser modificada
lanche[3] = 'picole' 

#? Acrescentando elementos
lanche.append('Cookie') # Adiciona um novo elemento
lanche.insert(2, 'refrigerante') # Adiciona um novo elemento e escolhe sua posição

#? Deletando elementos
del lanche[0] # Não é um metódo, e sim um comando
lanche.pop(3) # Apaga o elemento indicado da lista
lanche.remove('refrigerante') # Apaga o elemento indicando o valor
# Elimina o item e seu indice e reposiciona a contagem dos indíces

#? Estrutura de controle para lista
if 'pudim' in lanche: # Verifica se há o item na lista
    lanche.remove('pudim')
print(f'Lista de lanche atualziada: {lanche}')
print('-' * 60)

#? Estrutura de repetição
for c, v in enumerate(valores):
    print(f'Numero: {v}... posição: {c}')
print('-' * 60)

for cont in range(0,5): 
    lista.append(int(input('Insira um valor para lista: '))) # Adicionar itens a partir de input
print(f'Lista criada de inputs: {lista}')
print('-' * 60)

#? Ordenando valores da lista
numeros = [8, 2, 5, 4, 9, 3, 0]
print(f'Lista desordenada: {numeros}')
numeros.sort()
print(f'Lista ordenada crescente: {numeros}')
numeros.sort(reverse=True)
print(f'lista ordernada decrescente: {numeros}')
print('-' * 60)

#? Ligação de listas
a = [3, 6, 8, 12]
b = a # Listas interligadas, se mudar uma muda também a outra
copia = a[:] # Cria uma cópia da lista
b[2] = 9
print(f'Lista a: {a}')
print(f'Lista b: {b}')
print(f'Lista copia dos elementos a: {copia}')
print('-' * 60)
