from time import sleep

def contador(i, f, p):
    print('-=' * 15)
    if p == 0:
        p = 1
    if p < 0:
        p *= -1
    print(f'Contagem de {i} a {f} de {p} em {p}')
    if i > f:
        f -= 1
        p *= -1
    else:
        f += 1
    for c in range(i, f, p):
        print(c, end=' ', flush=True)
        sleep(0.5)
    print('FIM')

contador(1, 10, 1)
contador(10, 0, -2)

print('-=' * 15)
print('Personalize o contador.')
i = int(input(f'{"Início: ":<10}'))
f = int(input(f'{"Fim: ":<10}'))
p = int(input(f'{"Passo: ":<10}'))
contador(i, f, p)
