import modulo as md # Importanto funções de outro arquivo 
from modulo import dobro # Importa somente a função dobro do modulo

#? Pacotes
from pacote import numeros # Importa a função números de um pacote maior
#* Pacotes serve para dividir um programa muito grande em tópicos

# Para usar, coloca o nome do arquivo e a função que deseja
num = int(input('Digite um número: '))
f = md.fatorial(num)
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é igual a {fat}')
print(f'O dobro de {num} é {dobro(num)}') 
