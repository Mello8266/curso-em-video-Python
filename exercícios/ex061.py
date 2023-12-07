termo = int(input('Insira o primeiro termo da PA: '))
razao = int(input('Insira a razão da PA: '))
decimo = termo + (10 - 1) * razao
cont = 1
print(decimo)
# for c in range(termo, decimo + razao, razao):
#     print(c, end=' - ')
while cont != 10:
    cont += 1
    
print('FIM')