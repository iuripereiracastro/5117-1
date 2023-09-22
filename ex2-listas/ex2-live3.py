"""
Se o valor do elemento da lista é >= 20
entao o valor do elemento da lista é dividido por 2
"""

list = [60, 50, 10, 20, 78, 15, 7, 48, 50]
print(list)
i = 0

# for num in list:
#     if num >= 20:
#         list[i] = num / 2
#
#     i = i + 1

novaLista = []

for numero in list:
    if numero >= 20:
        novaLista.append(numero / 2)
    else:
        novaLista.append(numero)

print(f'novaLista = {novaLista}')


for x in range(len(list)):
    if list[x] >= 20:
        list[x] = list[x] / 2

print(list)
