# random import necesario para el jugador del equipo opuesto
import random

# Tuplas para los puntos de salud y defensa del jugador y del oponente
jugador = (100, 100)  # (puntos de salud, puntos de defensa)
oponente = (100, 100)  # (puntos de salud, puntos de defensa)

# Diccionario de ataques
ataques = {
    "malicioso": (10, 20),  # (daño a Ps, daño a defensa)
    "placaje": (35, 0),  # (daño a Ps, daño a defensa)
    "ascuas": (20, 0),  # (daño a Ps, daño a defensa)
    "latigo": (10, 10)  # (daño a Ps, daño a defensa)
}

# Código de las batallas
while jugador[0] > 0 and oponente[0] > 0:
    # Ataque del jugador
    ataque_jugador = ""
    while not ataque_jugador:
        ataque_jugador = input("Ataque?: ").lower()
        if ataque_jugador in ataques:
            ataque_jugador = ataque_jugador
        else:
            print("Que estas haciendo?! tus ataques son: malicioso, látigo, placaje y ascuas")
            ataque_jugador = ""

    # Ataque del oponente
    ataque_oponente = random.choice(list(ataques.keys()))

    # Efectos de los ataques
    if ataque_jugador in ataques:
        oponente = (oponente[0] - ataques[ataque_jugador][0], oponente[1] - ataques[ataque_jugador][1])

    # Verificación de ganador
    if oponente[0] <= 0:
        # mensajes finales de victoria/derrota
        print("Felicidades, has ganado")
    elif jugador[0] <= 0:
        print("Lo siento, has perdido")

