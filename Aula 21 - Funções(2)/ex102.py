def fatorial(a, show=False):
    '''
    -> Função que calcula o fatorial de um número
    :param a: O número a ser calculado
    :param show: (Opcional) Mostrar ou não a conta
    :return: Retorna o valor fatorial de um número a
    '''
    cont = a
    resultado = 1
    while cont > 0:
        if show == True:
            print(f'{cont}', end='')
            print(' x ' if cont > 1 else ' = ', end='')
        resultado *= cont
        cont -= 1
    print(resultado)
    return a

fatorial(5, show=True)