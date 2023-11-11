sal = float(input('Insira seu salário: R$'))

if sal >= 1250:
    aum = sal * 1.10

else:
    aum = sal * 1.15

print('Parabéns você recebeu um aumento!')
print('Seu sálario foi de R${:.2f} para R${:.2f}'.format(sal, aum))