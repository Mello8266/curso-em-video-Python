# Dicionário é uma variavel composta, a diferença dela é que ela tem indices literáis

#? declarar dicionário
dicionario = {} 
dicionario  = dict()
dados = {'nome': 'Pedro', 'idade': 25} # mudando o indice numérico para texto
print(dados['nome'])
filme = {'titulo': 'Star Wars',
        'ano': 1977,
        'diretor': 'George Luccas',
}


#? Manipulando dicionário
dados['sexo'] = 'm' # Adiciona a variável 'm' num novo indice 'sexo'
dados['nome'] = 'Henrique' # Muda o valor da chave 'nome' para 'Henrique'
del dados['idade'] # Delete os itens com indíce 'idade'

#? Formas de retorna um dicionário
print(filme.values()) # Retorna os valores do dicionário
print(filme.keys()) # Retorna as chaves do dicionário
print(filme.items()) # Retorna todos itens do dicionário

#? Estruturas de repetição com dicionários
for k, v in filme.items():
    print(f'O {k} é {v}')

#? Lista composta por um dicionário
brasil = list()
est1 = {'uf': 'Bahia', 'sigla': 'BA'}
est2 = {'uf': 'Minas Gerais', 'sigla': 'MG'}
brasil.append(est1)
brasil.append(est2)
print(brasil[1]['sigla'])

#? Lista composta com dicionário utilizando estrutura de repetição
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) # Adiciona uma cópia dos dados do dicionário na lista
for e in brasil: # e recebe um dicionário a cada repetição
    for k, v in e.items(): # k recebe uma key e v um valor
        print(f'{k}: {v}')

# Outra maneira
for e in brasil:
    for v in e.values():
        print(f'{v} - ', end='')
