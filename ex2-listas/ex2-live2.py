"""
Exercicio: list com n casas saber o maior e a sua posicao
"""

list = [20, 59, 19, 39, 40, 69, 79, 68, 92, 17]
maior = list[0]
i = 0
x = 0

for num in list:
    if num > maior:
        maior = num
        pos = list.index(num)
        x = i
    i = i + 1

print(f'O maior numero é: {maior}\nNa casa: {pos}')
print(f'O maior numero é: {maior}\nNa casa: {x}')
