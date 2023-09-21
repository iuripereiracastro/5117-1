"""
Se o valor do elemento da lista é >= 20
entao o valor do elemento da lista é dividido por 2
"""

list = [60, 50, 10, 20, 78, 15, 7, 48, 50]
print(list)
i = 0

for num in list:
    if num >= 20:
        list[i] = num / 2

    i = i + 1

print(list)
