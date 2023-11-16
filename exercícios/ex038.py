print('Insira dois valores e o computador ira analisa-los!')
num1 = int(input('Primerio valor: '))
num2 = int(input('Segundo valor: '))

if num1 > num2:
    print(f'O primeiro valor {num1} é maior que o segundo {num2}')

elif num2 > num1:
    print(f'O segundo valor {num2} é maior que o primeiro {num1}')

else:
    print(f'Os valores são iguais {num1} = {num2}')