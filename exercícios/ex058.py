from random import randint
from time import sleep

cores = {'limpa':'\033[m',
         'verde':'\033[32m',
         'vermelho':'\033[31m',
         'amarelo':'\033[33m'}

c = 0
p = randint(1, 10)
print('''Adivinhe o número que estou pensando!''')

f = True
while f == True:
    t = int(input(f'Insira um número entre 1 e 10: {cores["verde"]}'))
    p = randint(1, 10)

    if t > 10 or t <= 0:
        print(f'{cores["vermelho"]}ERROR-- \n{cores["limpa"]}Insira um número válido!\n')

    else:
        c += 1
        print(f'{cores["limpa"]}\nProcessando...\n')
        sleep(0.5)
        if t != p:
            print('Você errou HAHAHAHAHA.')
            print(f'Eu pensei em {cores["vermelho"]}{p}{cores["limpa"]}\n')
    if t == p:
        f = False

print(f'Você acertou... Eu e você pensamos no {cores["verde"]}{p}{cores["limpa"]}')
if c > 5:
    print(f'Só teve que tentar {cores["amarelo"]}{c}{cores["limpa"]} vezes, fraco.')
else: 
    print(f'Tentou advinhar {cores["amarelo"]}{c}{cores["limpa"]} vezes')