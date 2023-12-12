# Menu de opções - mini calculadora
from time import sleep

cores = {'limpa': '\033[m',
         'vermelho': '\033[32m'}

print('Insira dois números e faça alguma operação entre eles!')

# Recebe dois valores para utilizar no menu
n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))

# Entra na repetição
while True:
    # Escolhas do menu
    print('\nEscolha uma opção: \n[1] | somar \n[2] | multiplicar \n[3] | nº maior \n[4] | novos números \n[5] | sair do programa')
    es = str(input('Insira a opção: '))
    
    if es == '1':
        print(f'\n{cores["vermelho"]} {n1} + {n2} = {n1 + n2:.2f} {cores["limpa"]}')

    elif es == '2':
        print(f'\n{cores["vermelho"]} {n1} * {n2} = {n1 * n2:.2f} {cores["limpa"]}')

    elif es == '3':
        maior = n1
        if maior < n2:
            maior = n2
        print(f'\n{cores["vermelho"]} O {maior} é o maior número {cores["limpa"]}')

    elif es == '4':
        n1 = float(input('\nPrimeiro número: '))
        n2 = float(input('Segundo número: '))

    elif es == '5':
        break

    else:
        print('Valor inválido!')
    sleep(1.5)

print('Fim do programa!')