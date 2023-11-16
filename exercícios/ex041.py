dtNasc = int(input('Insira sua data de nascimento: '))
idade = 2023 - dtNasc

if idade <= 9:
    print('Categoria mirim')

elif idade > 9 and idade <= 14:
    print('Categoria infantil')

elif idade > 14 and idade <= 20:
    print('Categoria sênior')

else:
    print('Categoria master')