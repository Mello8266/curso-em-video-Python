def voto(num):
    from datetime import date
    idade = date.today().year - num
    if num > 18:
        return f'Com {idade} anos: O VOTO É OBRIGATÓRIO!'
    elif num >= 16 or num >= 65:
        return f'Com {idade} anos: O voto é opcional'
    else:
        return f'Com {idade} anos: O VOTO É NEGADO'

nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))