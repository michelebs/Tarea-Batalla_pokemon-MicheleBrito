#random import necesario para el jugador del equipo opuesto
import random

#Batalla
Ps_jugador = 100
Ps_oponente = 100 #Ps: puntos de salud
defensa_oponente = 100
defensa_jugador = 100

# Diccionario de ataques
ataques = {
    "malicioso": {"daño": 10, "efecto": "disminuye la defensa del oponente"},
    "placaje": {"daño": 35, "efecto": "no tiene efecto secundario"},
    "ascuas": {"daño": 20, "efecto": "quema al oponente"},
}

# Código de las batallas
while Ps_jugador > 0 and Ps_oponente > 0:
    #Ataque del jugador
    ataque_jugador = ""
    while not ataque_jugador:
        ataque_jugador = input("Ataque?: ").lower()
        if ataque_jugador in ataques:
            ataque_jugador = ataque_jugador
        else:
            print("Que estas haciendo?! tus ataques son: malicioso, placaje y ascuas")
            ataque_jugador = ""

    #Ataque del oponente
    ataque_oponente = random.randrange(1, 4)

    #Efectos de los ataques
    if ataque_jugador == "malicioso":
        defensa_oponente -= ataques[ataque_jugador]["daño"]
    elif ataque_jugador == "placaje":
        Ps_oponente -= ataques[ataque_jugador]["daño"] * 100 / defensa_oponente / 100
    elif ataque_jugador == "ascuas":
        Ps_oponente -= ataques[ataque_jugador]["daño"]

    #Verificación de ganador
    if Ps_oponente <= 0:
        #mensajes finales de victoria/derrota
        print("Felicidades, has ganado")
    elif Ps_jugador <= 0:
        print("Lo siento, has perdido")

        