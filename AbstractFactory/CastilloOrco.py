from AbstractFactory.CastilloAbstracto import CastilloAbstracto
from PersonajesSprites import PersonajesSprites


class CastilloOrco(CastilloAbstracto):

    def spritesCastillo(self):
        Castillo = []
        for i in range(0, 3):
            imagen = 'Imagenes/Castillos/CastilloVerde' + str(i + 1) + '.png'
            Castillo.append(PersonajesSprites(imagen, (300, 400)))

        return Castillo

    def spritesIconos(self):
        Iconos = []
        for i in range(0, 3):
            imagen = 'Imagenes/Iconos/Guerrero/Guerrero' + str(i + 1) + '.png'
            Iconos.append(PersonajesSprites(imagen, (50, 50)))

        return Iconos

    def coordenadas(self, jugador1, x, y):

        if jugador1:
            return (x, y)

        else:
            return (x, y)
