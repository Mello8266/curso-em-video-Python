import math

angulo = float(input('Insira o ângulo: '))
seno = math.sin(math.radians(angulo))
coseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('O ângulo de {} tem o seno de {:.2f} e cosseno de {:.2f} e a tangente {:.2f}'.format(angulo, seno, coseno, tangente))