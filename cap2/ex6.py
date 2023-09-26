import random

x = []
i = 0

while i < 3:
    x.append(random.randint(1, 100))
    i += 1

maior = x[0]
menor = x[0]

for n in x:
    if maior < n:
        maior = n
    if menor > n:
        menor = n

print(f'{x}\nMaior: {maior}\nMenor: {menor}')
