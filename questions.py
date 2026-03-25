# Punto 3: Programa que solicita un número y muestra su tabla de multiplicar del 1 al 10
numero = int(input("Ingresá un número para ver su tabla de multiplicar: "))

print(f"\nTabla del {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")