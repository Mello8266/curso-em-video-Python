print('Conversão númerica')
escolha = int(input('''Escolha uma dessas conversões:\n[1] para binário\n[2] para octal \n[3] para hexadecimal:\nSua opção: '''))
num = int(input('Isira um número inteiro: '))

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