termo = int(input('Insira o primeiro termo da PA: '))
razao = int(input('Insira a razão da PA: '))

for c in range(termo, termo * 10 + 1, razao):
    print(c)