from math import sqrt
from math import pow
from math import hypot

adj = float(input('Digite a medida do cateto adjacente: '))
opo = float(input('Digite a medida do cateto oposto: '))
hipo = sqrt(pow(adj,2) + pow(opo,2))
hip = hypot(adj, opo)
#print('h² = {}² + {}² é igual a {:.2f}\n'.format(adj, opo, hipo))
print(hip)
