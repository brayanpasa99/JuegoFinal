from random import choice, randrange

from Builder.CaracteristicasElfo import CaracteristicasElfo
from Builder.CaracteristicasGuerrero import CaracteristicasGuerrero
from Builder.CaracteristicasOrco import CaracteristicasOrco
from Builder.Director import Director
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

        if razaJugador1 == 'Orcos':
            concrete_builder = CaracteristicasOrco()
            director = Director()
            director.setBuilder(concrete_builder)
            product_final = director.getInterface()

        elif razaJugador1 == 'Elfos':
            concrete_builder = CaracteristicasElfo()
            director = Director()
            director.setBuilder(concrete_builder)
            director.getInterface()

        elif razaJugador1 == 'Guerreros':
            concrete_builder = CaracteristicasGuerrero()
            director = Director()
            director.setBuilder(concrete_builder)
            director.getInterface()

        else:
            print "Ingreso una raza incorrecta"

        print "Jugador 1 creado con la raza: "+razaJugador1

        print "Selecciona la raza del jugador 2:"
        print "1. Elfos"
        print "2. Orcos"
        print "3. Guerreros"

        razaJugador2 = raw_input()

        if razaJugador2 == 'Orcos':
            concrete_builder = CaracteristicasOrco()
            director = Director()
            director.setBuilder(concrete_builder)
            director.getInterface()

        elif razaJugador2 == 'Elfos':
            concrete_builder = CaracteristicasElfo()
            director = Director()
            director.setBuilder(concrete_builder)
            director.getInterface()

        elif razaJugador2 == 'Guerreros':
            concrete_builder = CaracteristicasGuerrero()
            director = Director()
            director.setBuilder(concrete_builder)
            director.getInterface()

        else:
            print "Ingreso una raza incorrecta"

        print "Jugador 2 creado con la raza: "+razaJugador2

    inicia.main()


if __name__ == "__main__":
    main()
