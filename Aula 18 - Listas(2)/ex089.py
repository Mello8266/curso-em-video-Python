# alunos [nome[notas]]
alunos = list()
nome = list()
notas = list()

while True:
    nome.append(str(input('Nome do aluno: ')))
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    nome.append(notas[:])
    alunos.append(nome[:])
    if len(notas) == 2:
        notas.clear()
        nome.clear()
    conf = str(input('Deseja continuar? ')).strip().upper()[0]
    if conf in 'N':
        break
print(f'{"Nº":3} {"NOME":<15} {"MÉDIA"}')
print('-' * 25)

n = 0
for c in alunos:
    print(f'{n:<3} {c[0]}',end='\n')
    n += 1