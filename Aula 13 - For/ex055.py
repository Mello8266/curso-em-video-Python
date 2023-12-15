print('Insira o peso de 5 pessoas, e o progama irá guardar o maior peso lido e o menor.')
print('-' * 20)

maiorpeso = 0
menorpeso = 0
for c in range(1, 6):
    peso = float(input(f'Peso da {c}ª pessoa: '))
    print('')

    if c == 1:
        maiorpeso = peso
        menorpeso = peso
    
    else:
        if peso > maiorpeso:
            maiorpeso = peso

        if peso < menorpeso:
            menorpeso = peso

print(f'Maior peso: {maiorpeso:.2f}Kg')
print(f'Menor peso: {menorpeso:.2f}Kg')