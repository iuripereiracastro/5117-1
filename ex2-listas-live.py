"""
Exercicio com lista ( = a um array )


# Lista vazia
lista = []

# Adiciona elementos a lista

lista.append(1)
lista.append(2)
lista.append(3)
lista.append(4)
lista.append(5)

print(lista)

# Remove os elementos 3 e 6
if 3 in lista:
    lista.remove(3)
if 6 in lista:
    lista.remove(6)

print(lista)
"""

lista = [10, 20, 30, 40, 50]
"""
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])
"""

for num in lista:
    print(num)
