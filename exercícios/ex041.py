from datetime import date

dtNasc = int(input('Insira sua data de nascimento: '))
atual = date.today().year
idade = atual - dtNasc

if idade <= 9:
    print('Categoria mirim')

elif idade <= 14:
    print('Categoria infantil')

elif idade <= 25:
    print('Categoria sênior')

else:
    print('Categoria master')