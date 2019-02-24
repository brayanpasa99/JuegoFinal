from AbstractFactory.GuerreroAbstracto import GuerreroAbstracto
from PersonajesSprites import PersonajesSprites


class Guerrero1(GuerreroAbstracto):

    def Atacar(self):
        SpritesAtacar = []
        for i in range(0, 8):
            imagen = 'Imagenes/Guerreros/Guerrero1/Ataque/Ataque' + str(i + 1) + '.png'
            SpritesAtacar.append(PersonajesSprites(imagen))

        return SpritesAtacar

    def Caminar(self):
        SpritesCaminar = []
        for i in range(0, 7):
            imagen = 'Imagenes/Guerreros/Guerrero1/Caminar/Caminar' + str(i + 1) + '.png'
            SpritesCaminar.append(PersonajesSprites(imagen))

        return SpritesCaminar

    def Muerte(self):
        SpritesMuerte = []
        for i in range(0, 7):
            imagen = 'Imagenes/Guerreros/Guerrero1/Muerte/Muerte' + str(i + 1) + '.png'
            SpritesMuerte.append(PersonajesSprites(imagen))

        return SpritesMuerte


