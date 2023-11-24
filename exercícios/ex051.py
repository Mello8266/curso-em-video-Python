termo = int(input('Insira o primeiro termo da PA: '))
razao = int(input('Insira a razão da PA: '))
decimo = termo + (10 - 1) * razao
for c in range(termo, decimo + razao, razao):
    print(c, end=' - ')
print('FIM')