# Declaração das listas
total = list()
par = list()
impar = list()

# Inserindo valores por um input na lista geral
while True:
    total.append(int(input('Insira um valor: ')))
    print('Valor adicionado.')
    conf = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if conf in 'N':
        # Analisando cada número da lista total
        for n in total:
            if n % 2 == 0: 
                par.append(n) # Adicionado o número par 
            else:
                impar.append(n) # Adicionado o número ímpar
        break
par.sort()
impar.sort()
print(f'você digitou os valores: {total}')
print(f'Valores pares digitados: {par}')
print(f'Valores impares digitados: {impar}')
