from datetime import date

dado = dict()
dado['nome']  = str(input('Insira o nome: ')).strip().capitalize()
data = int(input('Insira a data de nascimento: '))
dado['idade'] = date.today().year - data
dado['ctps'] = int(input('Carteira de trabalho (0 não tem): ')) 
if dado['ctps'] > 0:
    dado['contrato'] = int(input('Ano de contratação: '))
    dado['salario'] = float(input('Salário: R$'))
    dado['aposentadoria'] = dado['idade'] + ((dado['contrato'] + 35) - date.today().year)
for k, v in dado.items():
    print(f'  - {k} tem o valor {v}')
