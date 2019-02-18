import random

CASTILLOS = ['CastilloBlanco.png', 'CastilloRojo.png', 'CastilloVerde.png']


class Castillo():

    def castilloInicial(self):

        return CASTILLOS[random.randrange(3)]


