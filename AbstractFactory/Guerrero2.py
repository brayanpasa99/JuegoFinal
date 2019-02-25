from AbstractFactory.GuerreroAbstracto import GuerreroAbstracto
from PersonajesSprites import PersonajesSprites


class Guerrero2(GuerreroAbstracto):

    def Atacar(self):
        SpritesAtacar = []
        for i in range(0, 7):
            imagen = 'Imagenes/Guerreros/Guerrero2/Ataque/Ataque' + str(i + 1) + '.png'
            SpritesAtacar.append(PersonajesSprites(imagen, (50, 50)))

        return SpritesAtacar

    def Caminar(self):
        SpritesCaminar = []
        for i in range(0, 7):
            imagen = 'Imagenes/Guerreros/Guerrero2/Caminar/Caminar' + str(i + 1) + '.png'
            SpritesCaminar.append(PersonajesSprites(imagen, (50, 50)))

        return SpritesCaminar

    def Muerte(self):
        SpritesMuerte = []
        for i in range(0, 7):
            imagen = 'Imagenes/Guerreros/Guerrero2/Muerte/Muerte' + str(i + 1) + '.png'
            SpritesMuerte.append(PersonajesSprites(imagen, (50, 50)))

        return SpritesMuerte
