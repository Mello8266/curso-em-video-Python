# Gerador de PA recusirva
termo = int(input('Insira o primeiro termo da PA: '))
razao = int(input('Insira a razão dessa PA: '))
cont = 1
m = 10
contador = 1

while m > 0:
    print(termo, end=' ')
    termo += razao
    cont += 1
    contador += 1
    if cont > m:
        m = int(input('\nQuer ver mais quantos termos dessa PA? '))
        cont = 1
print(f'Fim do programa, mostrou {contador - 1} termos')
