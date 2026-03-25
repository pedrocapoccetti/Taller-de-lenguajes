import random

categorias = {
    "programacion": ["python", "variable", "funcion", "bucle"],
    "animales": ["perro", "gato", "elefante", "jirafa"],
    "comida": ["pizza", "pasta", "asado", "empanada"]
}

print("¡Bienvenido al Ahorcado!")

seguir_jugando = "si"

while seguir_jugando == "si":
    print()
    print("Categorías disponibles:")
    for categoria in categorias:
        print("-", categoria)

    categoria_elegida = input("Elegí una categoría: ").lower()

    while categoria_elegida not in categorias:
        print("Categoría inválida")
        categoria_elegida = input("Elegí una categoría: ").lower()

    # 🔥 NO REPETIR PALABRAS
    palabras_disponibles = random.sample(categorias[categoria_elegida], len(categorias[categoria_elegida]))

    for word in palabras_disponibles:
        guessed = []
        attempts = 6

        print()
        print("Nueva palabra!")

        while attempts > 0:
            progress = ""
            for letter in word:
                if letter in guessed:
                    progress += letter + " "
                else:
                    progress += "_ "
            print(progress)

            if "_" not in progress:
                print("¡Ganaste!")
                break

            print(f"Intentos restantes: {attempts}")
            print(f"Letras usadas: {', '.join(guessed)}")

            letter = input("Ingresá una letra: ").lower()

            if len(letter) != 1 or not letter.isalpha():
                print("Entrada no válida")
                print()
                continue

            if letter in guessed:
                print("Ya usaste esa letra.")
            elif letter in word:
                guessed.append(letter)
                print("¡Bien! Esa letra está en la palabra.")
            else:
                guessed.append(letter)
                attempts -= 1
                print("Esa letra no está en la palabra.")

            print()

        else:
            print(f"¡Perdiste! La palabra era: {word}")

    seguir_jugando = input("¿Querés jugar otra ronda? (si/no): ").lower()

print("Gracias por jugar!")