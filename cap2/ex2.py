dist = float(input(f'Distancia a percorrer (kilometros): '))
temp = int(input(f'Tempo que demora (minutos):'))
horas = temp / 60
segundos = temp * 60
metros = dist * 1000

print(f'Velocidade a Km/h: {dist / horas}')
print(f'Velocidade a m/s: {metros / segundos}')
