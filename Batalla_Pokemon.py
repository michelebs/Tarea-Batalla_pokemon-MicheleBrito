#random import neecsario para el jugador del equipo opuesto
import random

#Batalla
Ps_jugador=100
Ps_oponente=100 #Ps: puntos de salud
defensa_oponente=100
defensa_jugador=100

# Código de las batallas
print("-----------------------------------------------------------------")
while Ps_jugador>0  and Ps_oponente>0:
    ataque_jugador=""
    while not ataque_jugador:
        ataque_jugador=input("Ataque?: ")
    if ataque_jugador=="malicioso":
        defensa_oponente -= 10
    elif ataque_jugador=="placaje":
        Ps_oponente-=35 / defensa_oponente/100
    elif ataque_jugador=="ascuas":
        Ps_oponente-=20
    else:
        print("Que estas haciendo?!  tus ataques son: malicioso, placaje y ascuas")
        ataque_jugador=""
        print("-----------------------------------------------------------------")
    ataque_oponente=random.randrange(1,3+1)
    if  ataque_oponente==1:
        defensa_jugador-=10
    elif ataque_oponente==2:
        Ps_jugador-=35 / defensa_oponente/100
    elif ataque_jugador==3:
        Ps_jugador-=20
if Ps_oponente<=0: #mensajes finales de victoria/derrota
    print("Felicidades, has ganado")
elif Ps_jugador<=0:
    print("Lo siento, has perdido")
    print("-----------------------------------------------------------------")