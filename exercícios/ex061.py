termo = int(input('Insira o primeiro termo da PA: '))
razao = int(input('Insira a razão da PA: '))
decimo = termo + (10 - 1) * razao
while termo != decimo:
    print(termo, end=' ')
    termo += razao
print(f'{termo}')