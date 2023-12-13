# Tratando valores com uma flag de interrompimento
cont = s = 0
while True:
    n = int(input('Insira um valor [999 para a aplicação]: '))
    if n == 999:
        break
    cont += 1
    s += n
text = str(f'A soma dos {cont} valores digitados é: {s}')
if cont == 1:
    print(text.replace('dos', 'de').replace('valores', 'valor').replace('digitados', 'digitado'))
else:
    print(text)
    