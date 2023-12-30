from time import sleep

def contador(i, f, p):
    print('-=' * 15)
    for c in range(i, f, p):
        print(c, end=' ')
        sleep(0.5)
    print('FIM')

print('Contagem de 1 a 10 de 1 em 1')
contador(1, 11, 1)

print('Contagem de 10 a 1 de 2 em 2')
contador(10, -1, -2)

print('-=' * 15)
print('Personalize o contador.')
i = int(input(f'{"Início: ":<10}'))
f = int(input(f'{"Fim: ":<10}'))
p = int(input(f'{"Passo: ":<10}'))
if p == 0:
    p = 1
if p < 0:
    p *= -1

print(f'Contagem de {i} a {f} de {p} em {p}')
if i > f:
    contador(i, f -1, -p)
else:
    contador(i, f + 1, p)