# Punto 2: Convertir una cantidad de segundos a horas, minutos y segundos
segundos_totales = int(input("Ingresá la cantidad de segundos: "))

horas = segundos_totales // 3600
minutos = (segundos_totales % 3600) // 60
segundos_restantes = segundos_totales % 60

print(f"{segundos_totales} segundos equivalen a:")
print(f"{horas} horas, {minutos} minutos y {segundos_restantes} segundos.")