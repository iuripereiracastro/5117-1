"""
Lista: Quantidade de numeros entre 0 e 10; 11 e 20; 21 e 30; 31 e 40; 41 e 50; 50+
                                     a        b        c        d        e      f
"""

list = [60, 20, 40, 39, 10, 25, 40, 239, 10, 59, 28, 29, 200]
counter = [0, 0, 0, 0, 0, 0]
#          0  1  2  3  4  5

a = 0
b = 0
c = 0
d = 0
e = 0
f = 0

for num in list:
    if num <= 10:
        a += 1
        counter[0] += 1
    elif num <= 20:
        b += 1
        counter[1] += 1
    elif num <= 30:
        c += 1
        counter[2] += 1
    elif num <= 40:
        d += 1
        counter[3] += 1
    elif num <= 50:
        e += 1
        counter[4] += 1
    else:
        f += 1
        counter[5] += 1

print(f'Numeros entre 0 a 10: {a}\nNumeros entre 11 a 20: {b}\nNumeros entre 21 a 30: {c}\nNumeros entre 31 a 40: {d}\nNumeros entre 41 a 50: {e}\nNumeros maior que 50: {f}')

#        'começa em 0' e acaba na length da lista
for x in range(0, len(counter)):
    print(f'counter[{x}] = {counter[x]}')
