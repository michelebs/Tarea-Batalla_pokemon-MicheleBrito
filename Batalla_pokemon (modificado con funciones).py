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

# Funciones de ataques
def ataque_jugador_malicioso(salud, defensa):
    return (salud - ataques["malicioso"][0], defensa - ataques["malicioso"][1])

def ataque_jugador_placaje(salud, defensa):
    return (salud - ataques["placaje"][0], defensa - ataques["placaje"][1])

def ataque_jugador_ascuas(salud, defensa):
    return (salud - ataques["ascuas"][0], defensa - ataques["ascuas"][1])

def ataque_jugador_latigo(salud, defensa):
    return (salud - ataques["latigo"][0], defensa - ataques["latigo"][1])

# Código de las batallas
while jugador[0] > 0 and oponente[0] > 0:
    # Ataque del jugador
    ataque_jugador = ""
    while not ataque_jugador:
        ataque_jugador = input("Ataque?: ").lower()
        if ataque_jugador in ataques:
            if ataque_jugador == "malicioso":
                jugador = ataque_jugador_malicioso(jugador[0], jugador[1])
            elif ataque_jugador == "placaje":
                jugador = ataque_jugador_placaje(jugador[0], jugador[1])
            elif ataque_jugador == "ascuas":
                jugador = ataque_jugador_ascuas(jugador[0], jugador[1])
            elif ataque_jugador == "latigo":
                jugador = ataque_jugador_latigo(jugador[0], jugador[1])
        else:
            print("¡Qué estás haciendo?! Tus ataques son: malicioso, látigo, placaje y ascuas")
            ataque_jugador = ""

    # Ataque del oponente
    ataque_oponente = random.choice(list(ataques.keys()))

    # Efectos de los ataques
    if ataque_oponente in ataques:
        jugador = (jugador[0] - ataques[ataque_oponente][0], jugador[1] - ataques[ataque_oponente][1])

    # Verificación de ganador
    if oponente[0] <= 0:
        # mensajes finales de victoria/derrota
        print("Felicidades, has ganado")
    elif jugador[0] <= 0:
        print("Lo siento, has perdido")