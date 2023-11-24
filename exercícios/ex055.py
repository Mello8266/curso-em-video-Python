print('Insira o peso de 5 pessoas, e o progama irá guardar o maior peso lido e o menor.')
print('-' * 20)

maiorpeso = 0
menorpeso = 300
for c in range(0, 5):
    peso = float(input('Peso: '))
    print('')

    if peso > maiorpeso:
        maiorpeso = peso
    
    if peso < menorpeso:
        menorpeso = peso

print(f'Maior peso: {maiorpeso}')
print(f'Menor peso: {menorpeso}')