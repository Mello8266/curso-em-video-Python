def leiaInt(txt):
    while True:
        try:
            inteiro = int(input(txt))
        except ValueError:
            print('\033[31mErro! Digite um número válido.\033[m')
        except KeyboardInterrupt:
            print('\033[31mErro! O usuário decidiu não informar nenhum dado.\033[m')
            inteiro = 0
            return inteiro
        else:
            return inteiro

def leiaFloat(txt):
    while True:
        try:
            real = float(input(txt))
        except ValueError:
            print('\033[31mErro! Digite um número válido.\033[m')
        except KeyboardInterrupt:
            print('\033[31mErro! O usuário decidiu não informar nenhum dado.\033[m')
            real = 0
            return real
        else:
            return real
        

n = leiaInt('Digite um número inteiro: ')
r = leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado {n} o real {r}')