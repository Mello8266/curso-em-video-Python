# PA de 10 termos
termo = int(input('Insira o primeiro termo da PA: '))
razao = int(input('Insira a razão da PA: '))
count = 1
while count <= 10:
    print(f'{count}º termo: {termo}')
    termo += razao
    count += 1
print('fim')