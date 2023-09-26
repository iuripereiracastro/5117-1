seg = int(input(f'Escreva um número de segundos\n'))
minutos = int(seg / 60)
horas = int(minutos / 60)
dias = int(horas / 24)

print(f'dias: {dias} || horas: {horas % 24} || mins: {minutos % 60} || segs: {seg % 60}')
