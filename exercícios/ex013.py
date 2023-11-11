print('Aumento de 15% no salário')

sal = float(input('Insira o salário atual: '))

aum = sal * 1.15

#outro jeito
novo = sal + (sal * 15 / 100)

print('Seu novo salário é {:.2f}'.format(novo))
