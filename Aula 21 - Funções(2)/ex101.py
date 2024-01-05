from datetime import date 
def voto(num):
    if num > 18:
        return 'O VOTO É OBRIGATÓRIO!'
    elif num >= 16 or num >= 65:
        return 'O voto é opcional'
    else:
        return 'O VOTO É NEGADO'

nasc = int(input('Insira o ano em que nasceu: '))
idade = date.today().year - nasc
print(f'Com {idade} anos {voto(idade)}')