"""
O primeiro soma x1+x2+x3+x4+x5 (sendo que cada x é um dos 5 números que o user meteu)
O segundo é (x1-x̄)²+(x2-x̄)²+(x3-x̄)²...
"""
from math import sqrt

x = []
i = 0

while i < 5:
    x.append(int(input('Insira um numero\n')))
    i += 1

media = 0
for n in x:
    media += n
media = media / len(x)

desvio = 0
for n in x:
    desvio += (n - media) ** 2
desvio = sqrt((1/4)*desvio)

print(f'Media: {media}\nDesvio padrao: {desvio}')
