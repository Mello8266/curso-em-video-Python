def separador(txt):
    '''
    -> Linha para separar os conteúdos
    '''
    print('-=' * 20)
    print(f'{txt:^40}')
    print('-=' * 20)

#? Interactives help
separador('Interactives help')
help(print) # Metódo que retorna o manual de uma funcionalidade
print(input.__doc__) # Outra forma

#? Docstrings
separador('Docstrings')
def contador(i, f, p):
    '''
    -> Faz uma contagem e exibe na tela
    :Param i: ínicio da contagem
    :Param f: fim da contagem
    :Param p: passo da contagem
    :return: sem retorno
    ''' # A string dentro dessas aspas é o manual da função - docstring
    for c in range(i, f, p):
        print(c, end=' ', flush=True)
    print('FIM')
help(contador)

#? Parâmetros opcionais
separador('Parâmetros opcionais')
def soma(a=0, b=0, c=0): # Na chamada da função pode informar de 0 a 3 valores
    s = a + b + c
    print(f'A soma vale {s}')
soma(1, 5)

#? Escopo das variáveis
separador('Escopo das variáveis')
a = 10
def teste():
    x = 0
    print(f'O a vale {a} na função teste')
    print(f'O x vale {x} na função teste')
teste()
print(f'O a vale {a} no programa principal, pois é uma variável global')
print('O x não está declarado de forma local, então só existe na função teste')

b = 1
def teste2():
    # global b usa a variável global ao invés de criar uma local
    b = 2
    print(f'b local vale {b}')
teste2()
print(f'b global vale {b}')

#? Retorno das variáveis
separador('Retorno das variáveis')
def soma(a=0, b=0, c=0):
    s = a + b + c
    return s # A função está retornando a soma
r1 = soma(1, 2, 3)
r2 = soma(1, 2)
r3 = soma(1)
print(f'O resultado das somas deu {r1}, {r2}, {r3}')

def par(num=0):
    if num % 2 == 0:
        return True
    else:
        return False # Pode retornar vários tipos de dados
num = int(input('Insira um número: '))
if par(num):
    print(f'O {num} é par')
else:
    print(f'O {num} é impar')