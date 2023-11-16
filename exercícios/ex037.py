print('Conversão númerica')
num = int(input('Isira um número inteiro: '))
escolha = int(input('Escolha uma dessas conversões: 1 para binário, 2 para octal ou 3 para hexadecimal: '))

if escolha == 1:
    str = bin(num)
    print(f'O número {num} em binário vale {str[2:]}')

elif escolha == 2:
    str = oct(num)
    print(f'O número {num} em octal vale {str[2:]}')

elif escolha == 3:
    string = hex(num)
    print(f'O número {num} em hexadecimal vale {string[2:]}')

else:
    print('EROO -- Insira uma opção válida!')