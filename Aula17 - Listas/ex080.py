# Organizando lista sem o sort()
numeros = list()

# Inserindo valores na lista
for c in range(0, 5):
    valor = int(input('Insira um valor: '))

    # Vericando se o valor é maior digitado
    if c == 0 or valor > numeros[-1]:
        print(f'Valor adicionado na última posição.')
        numeros.append(valor) # Se sim, ele é adicionado na última posição

    # Se ele é for menor, o programa analisa cada número da lista e procura o índice correto
    else:
        for cont, n in enumerate(numeros): # Contador é o índice
            if valor <= n:
                numeros.insert(cont, valor) # Adiciona o valor no índice correto
                print(f'Valor adicionado na posição {cont}.')
                break
print(numeros)
        