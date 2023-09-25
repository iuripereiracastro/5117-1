semanas = [1, 2, 3, 4]
dias = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta']

while y < len(semanas):
    x = 0
    while x < len(dias):
        # Semana 1 - Segunda
        # Semana 1 - Terça
        # ...
        print(f'Semana {semanas[y]} - {dias[x]}')
        x += 1
    y += 1
    print('-----------')
