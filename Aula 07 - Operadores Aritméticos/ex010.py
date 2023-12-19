print('Conversão de moeda')

reais = float(input('Quanto você quer converter? R$'))
moeda = input('Qual moeda você quer comprar:\ndolar \neuro \npeso argentino \nyuan \n:')

dolar = reais / 5.03
euro = reais / 5.34
arg = reais * 69.41
yuan = reais * 1.45 

if moeda == 'dolar':
    print('Você pode comprar US${:.2f} com R${:.2f}'.format(dolar, reais))

if moeda == 'euro':
    print('Você pode comprar €{:.2f} com R${:.2f}'.format(euro, reais))

if moeda == 'peso argentino':
    print('Você pode comprar ARS{:.2f} com R${:.2f}'.format(arg, reais))

if moeda == 'yuan':
    print('Você pode comprar ¥{:.2f} com R${:.2f}'.format(yuan, reais))
    
# Fonte: https://www.youtube.com/watch?v=_uQrJ0TkZlc&list=PLHz_AreHm4dlAnJ_jJtV29RFxnPHDuk9o&index=5