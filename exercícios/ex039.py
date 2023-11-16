from datetime import date

sexo = int(input('Informe seu sexo: 1 para masculino e 2 para feminino: '))
dt_nasc = int(input('Insira o ano que nasceu: '))

hoje = date.today()
idade = hoje - dt_nasc

if sexo == 2:
    print('Seu alistamento não é obrigatório!')

else:
    if idade == 18:
        print(f'Você já possui {idade} anos esse é o momento de se alistar!!!')

    elif idade < 18:
        falta = 18 - idade
        print(f'Está cedo jovem, volte daqui {falta} anos')

    else:
        dem = idade - 18
        print(f'Era pra ter se apresentado a {dem} ano. \nVENHA QUANTO ANTES!!')