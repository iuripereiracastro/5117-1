nota = []

n = 0
while n >= 0:
    n = float(input(f'Insira uma nota(0 a 20)\n(-1 para acabar de inserir)\n'))
    if n >= 0:
        nota.append(n)


posCounter = 0
for x in nota:
    if x >= 10:
        posCounter += 1


print(f'Percentagem de alunos com nota positiva: {round(posCounter / len(nota) * 100, 2)}%')
