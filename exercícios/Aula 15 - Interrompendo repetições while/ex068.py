# Par o ímpar com While
from random import randint
from time import sleep

text = {'limpa':'\033[m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'amarelo':'\033[33m',
         'azul': '\033[34m'}

print('=-=' * 20)
print('VAMOS JOGAR ÍMPAR OU PAR')

v = 0
while True:
    pc = randint(0, 10)
    print('=-=' * 20)
    pessoa = int(input('Diga um valor: '))
    ip = str(input('Impar ou par? [I/P] ')).strip().lower()[0]
    print('=-=' * 20)
    s = pc + pessoa
    print(f'Jogador: {text["azul"]}{pessoa}{text["limpa"]} Computador: {text["vermelho"]}{pc}{text["limpa"]}... Total {s} deu', end=' ')
    if s % 2 == 0:
        print(f'{text["amarelo"]}PAR{text["limpa"]}') 
        print('-' * 50)
        if ip in ('p'):
            (f'\n{text["azul"]}Você venceu!{text["limpa"]}')
            v += 1
        else:
            break
    else:
        print(f'{text["amarelo"]}IMPAR{text["limpa"]}')
        print('-' * 50)
        if ip in ('i'):
            (f'\n{text["azul"]}Você venceu!{text["limpa"]}')
            v += 1
        else:
            break
    print('~' * 50)
    print(f'{text["vermelho"]}VAMOS OUTRA ATÉ EU VENCER!{text["limpa"]}')
    print('~' * 50)
    print('')
    sleep(1.5)
print(f'GAME OVER! Total de vitórias: {v}')
   