n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

t = int(input('\nInsira um número entre 0 e 20: '))
while t < 0 or t > 20:
    t = int(input('ERROR--\nInsira um número entre 0 e 20: '))

print(f'Você digitou o número {n[t]}')
