from random import choice, randrange

from CampoBatalla.CampoBatallaMain import CampoBatallaMain
from Jugador import Jugador


def main():

    inicia = CampoBatallaMain()

    print "Menu:"
    print "1. Jugar"
    print "2. Salir"

    opcion = input()

    if opcion == 1:

        print "Selecciona la raza del jugador 1:"
        print "1. Elfos"
        print "2. Orcos"
        print "3. Guerreros"

        razaJugador1 = raw_input()
        jugador1 = Jugador(razaJugador1)

        print "Jugador 1 creado con la raza: "+razaJugador1

        print "Selecciona la raza del jugador 2:"
        print "1. Elfos"
        print "2. Orcos"
        print "3. Guerreros"

        razaJugador2 = raw_input()
        jugador2 = Jugador(razaJugador2)

        print "Jugador 2 creado con la raza: "+razaJugador2

    inicia.main()


if __name__ == "__main__":
    main()
