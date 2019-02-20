from random import choice, randrange

from CampoBatalla import CampoBatallaMain


def main():

    inicia = CampoBatallaMain.CampoBatallaMain()
    inicia.creaJugador(choice(['Orco', 'Elfo', 'Guerrero']), randrange(1000, 5000), range(100, 1000))
    inicia.creaJugador(choice(['Orco', 'Elfo', 'Guerrero']), randrange(1000, 5000), range(100, 1000))
    inicia.entregaAvatar()
    inicia.main()


if __name__ == "__main__":
    main()
