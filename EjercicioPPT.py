import random

def jugarPPT():
    while True:
        opciones = ["piedra", "papel", "tijera"]
        puntos_jugador, puntos_maquina = 0, 0

        while puntos_jugador < 3 and puntos_maquina < 3:
            jugador = input("Elige piedra, papel o tijera: ").lower()
            if jugador not in opciones:
                print("Opción no válida, intenta de nuevo.")
                continue

            maquina = random.choice(opciones)
            print(f"La máquina eligió: {maquina}")

            if jugador == maquina:
                print("Empate!")
            elif (jugador == "piedra" and maquina == "tijera") or \
                 (jugador == "papel" and maquina == "piedra") or \
                 (jugador == "tijera" and maquina == "papel"):
                puntos_jugador += 1
                print("Ganaste esta ronda!")
            else:
                puntos_maquina += 1
                print("La máquina gana esta ronda!")

            print(f"Puntaje: Jugador {puntos_jugador} - Máquina {puntos_maquina}\n")

        if puntos_jugador == 3:
            print("¡Felicidades, ganaste el juego!")
        else:
            print("La máquina ganó el juego. ¡Suerte la próxima vez!")

        jugar_de_nuevo = input("¿Quieres jugar otra vez? (s/n): ").lower()
        if jugar_de_nuevo != 's':
            print("Gracias por jugar. ¡Hasta la próxima!")
            break