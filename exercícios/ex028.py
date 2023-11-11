from random import randint
from time import sleep

pc = randint(0, 5)

print('-=-' * 20)
print('Pensarei em um número de 0 a 5, tente advinhar.')
print('-=-' * 20)

pessoa = int(input("Em que número estou pensando? "))
print('Processando...')
sleep(1.5)

print('')
if pc == pessoa:
    print('Você acertou! Pensei em {}'.format(pc))

else:
    print('Você errou,eu pensei em {} e você em {}, inferior.'.format(
        pc, pessoa))
