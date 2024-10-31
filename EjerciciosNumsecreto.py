import random

def numsecreto():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    print("¡Adivina el número entre 1 y 100!")

    while True:
        try:
            intento = int(input("Introduce tu intento: "))
            intentos += 1

            if intento < 1 or intento > 100:
                print("Por favor, elige un número entre 1 y 100.")
                continue

            if intento < numero_secreto:
                print("Demasiado bajo, intenta nuevamente.")
            elif intento > numero_secreto:
                print("Demasiado alto, intenta nuevamente.")
            else:
                print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
                break

        except ValueError:
            print("Por favor, ingresa un número válido.")