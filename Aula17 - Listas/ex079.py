# Declarando a lista e inserindo os valores
lista = list()
while True:
    valor = int(input('Insira um valor: '))

    # Verificando se o valor já está na lista
    if valor in lista:
        print('Valor duplicado! Não vou adicionar.')
    else:
        lista.append((valor))
        print('Valor adicionado!')
    conf = str(input('Deseja continuar? [S/N]: '))
    if conf in ('n'):
        break
lista.sort()
print(f'Você adicionou os valores: {lista}')