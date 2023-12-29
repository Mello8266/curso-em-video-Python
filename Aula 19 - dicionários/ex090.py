print(f'{"SITUAÇÃO DO ALUNO":^15}')
nome = str(input('Nome: ')).strip().capitalize()
media = float(input('Média do aluno: '))
cod = {'Nome': nome, 'Media': media}
if media >= 6:
    cod['Situação'] = 'aprovado'
else: 
    cod['Situação'] = 'desaprovado'
for k, v in cod.items():
    print(f'  - {k} é igual a {v}')
