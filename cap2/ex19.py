euros = [
    [50, 20, 10, 5],    # Notas
    [2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]  # Moedas
]
counter = [
    [0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]
euro = float(input(f'Insira uma quantia(Euros):\n'))
change = euro
print(change)

while change > 0:
    print(change)
    if change >= 5:
        x = 0
        if change >= euros[0][x]:
            change -= euros[0][x]
            counter[0][x] += 1
        else:
            x += 1
    elif change > 0:
        y = 0
        if change >= euros[1][y]:
            change -= euros[1][y]
            counter[1][y] += 1
        else:
            y += 1


for a in range(len(counter)):
    for b in range(len(counter[a])):
        if counter[a][b] > 0:
            print(counter[a][b])
