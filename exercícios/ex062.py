termo = int(input('Insira o primeiro termo da PA: '))
razao = int(input('Insira a razão da PA: '))
ult = int(input('Qual o último n da PA: '))
cont = 1
decimo = termo + (ult - 1) * razao
print(decimo)
while True:
    cont += 1
    if cont == 1 or termo == decimo:
        conf = str(input('\nDeseja continuar? [S/N]')).upper()
        if conf in ('S, SIM, SI'):
            ult = int(input('\nQual o último n da PA: '))
            decimo = termo + (ult - 1) * razao
        else:
            break
    print(termo, end=' ')
    termo += razao
