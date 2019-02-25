from Builder.Director import Director
from Builder.SpritesElfo1 import SpritesElfo1
from Builder.SpritesElfo2 import SpritesElfo2
from Builder.SpritesElfo3 import SpritesElfo3
from Builder.SpritesGuerrero1 import SpritesGuerrero1
from Builder.SpritesGuerrero2 import SpritesGuerrero2
from Builder.SpritesGuerrero3 import SpritesGuerrero3
from Builder.SpritesOrco1 import SpritesOrco1
from Builder.SpritesOrco2 import SpritesOrco2
from Builder.SpritesOrco3 import SpritesOrco3
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

        if razaJugador1 == '2':

            director = Director()
            Orcos = []
            for i in (SpritesOrco1(), SpritesOrco2(), SpritesOrco3()):
                director.setBuilder(i)
                Orcos.append(director.getSprites())
            jugador1 = Jugador(Orcos)

        elif razaJugador1 == '1':

            director = Director()
            Elfos = []
            for i in (SpritesElfo1(), SpritesElfo2(), SpritesElfo3()):
                director.setBuilder(i)
                Elfos.append(director.getSprites())
            jugador1 = Jugador(Elfos)

        elif razaJugador1 == '3':

            director = Director()
            Guerreros = []
            for i in (SpritesGuerrero1(), SpritesGuerrero2(), SpritesGuerrero3()):
                director.setBuilder(i)
                Guerreros.append(director.getSprites())
            jugador1 = Jugador(Guerreros)

        else:
            print "Ingreso una raza incorrecta"

        print "Jugador 1 creado con la raza: " + razaJugador1

        print "Selecciona la raza del jugador 2:"
        print "1. Elfos"
        print "2. Orcos"
        print "3. Guerreros"

        razaJugador2 = raw_input()

        if razaJugador2 == '2':

            director = Director()
            Orcos = []
            for i in (SpritesOrco1(), SpritesOrco2(), SpritesOrco3()):
                director.setBuilder(i)
                Orcos.append(director.getSprites())
            jugador2 = Jugador(Orcos)

        elif razaJugador2 == '1':

            director = Director()
            Elfos = []
            for i in (SpritesElfo1(), SpritesElfo2(), SpritesElfo3()):
                director.setBuilder(i)
                Elfos.append(director.getSprites())
            jugador2 = Jugador(Elfos)

        elif razaJugador2 == '3':

            director = Director()
            Guerreros = []
            for i in (SpritesGuerrero1(), SpritesGuerrero2(), SpritesGuerrero3()):
                director.setBuilder(i)
                Guerreros.append(director.getSprites())
            jugador2 = Jugador(Guerreros)

        else:
            print "Ingreso una raza incorrecta"

        print "Jugador 2 creado con la raza: " + razaJugador2

        inicia.main((jugador1, jugador2))


if __name__ == "__main__":
    main()
