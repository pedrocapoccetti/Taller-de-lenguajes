from datetime import date

# Punto 1: Solicitar año de nacimiento y calcular hitos de edad
anio_nacimiento = int(input("Ingresá tu año de nacimiento: "))

cumple_18 = anio_nacimiento + 18
cumple_21 = anio_nacimiento + 21
cumple_100 = anio_nacimiento + 100

print(f"Cumplirás 18 años en el año: {cumple_18}")
print(f"Cumplirás 21 años en el año: {cumple_21}")
print(f"Cumplirás 100 años en el año: {cumple_100}")