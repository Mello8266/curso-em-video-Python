import time
import random

cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'vermelho':'\033[31m'}

print('-=-' * 20)
print(f'Vamos jogar pedra, papel, tesoura.\n{cores["vermelho"]}Eu{cores["limpa"]} contra {cores["azul"]}você!{cores["limpa"]}')
print('-=-' * 20)

p1 = str(input('Pedra, papel ou tesora? ')).strip().lower()
pc = ['predra', 'papel', 'tesoura']
pc = random.choice(pc)

print('Processando...')
time.sleep(1.5)

print(f'{cores["azul"]}Você escolheu {p1}{cores["limpa"]} x {cores["vermelho"]}Eu escolhi {pc}{cores["limpa"]}')

if p1 == 'pedra' and pc == 'tesoura' or p1 == 'tesoura' and pc == 'papel' or p1 == 'papel' and pc == 'pedra':
    print(f'{cores["azul"]}Você venceu{cores["limpa"]}...\nteve sorte!')

else:
    print(f'Eu venci. {cores["vermelho"]}HAHAHAHAHAH{cores["limpa"]}')