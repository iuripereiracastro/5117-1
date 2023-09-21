"""
Lista: Quantidade de numeros entre 0 e 10; 11 e 20; 21 e 30; 31 e 40; 41 e 50; 50+
                                     a        b        c        d        e      f
"""

list = [60, 20, 40, 39, 10, 25, 40, 239, 10, 59, 28, 29]
counter = []

i = 0

a = 0
b = 0
c = 0
d = 0
e = 0
f = 0

a2 = 0
b2 = 0
c2 = 0
d2 = 0
e2 = 0
f2 = 0

for num in list:
    if num <= 10:
        a = a + 1
        counter[i] = a2 + 1
    elif num <= 20:
        b = b + 1
    elif num <= 30:
        c = c + 1
    elif num <= 40:
        d = d + 1
    elif num <= 50:
        e = e + 1
    else:
        f = f + 1
    i = i + 1

print(f'Numeros entre 0 a 10: {a}\nNumeros entre 11 a 20: {b}\nNumeros entre 21 a 30: {c}\nNumeros entre 31 a 40: {d}\nNumeros entre 41 a 50: {e}\nNumeros maior que 50: {f}')
