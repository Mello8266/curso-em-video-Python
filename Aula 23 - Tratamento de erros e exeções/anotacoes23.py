
#? Erro de exeção - exception
'''
Erro que não é sintático, ocorre ocasionalmente
'''

# print(x) #! Erro - NameError, problema pois a variável x não existe
n = int(input('Digite um número: ')) #! Erro caso digite algo que não seja um int - ValueError

#? Tratamento de erros
try: #* Tente o bloco de operação
    a = int(input('Numerador: '))
    b = int(input('Demonimador: '))
    r = a / b
except Exception as erro: #* Se não funcionar, aciona esse bloco de operação
    print(f'Problema encontrado foi {erro.__class__}')

#* Vários tipos de except, funcionando como um elif para cada caso
# except ValueError:
# except OSError:
# except TypeError: 
# except KeyboardInterrupt:

else: #* Se a operação funcionar corretamente
    print(f'Resultado da operação: {r}')
finally: #* Ocorre indenpedente se a operação falhar ou não
    print('Volte sempre')
