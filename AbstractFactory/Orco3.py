from AbstractFactory.OrcoAbstracto import OrcoAbstracto
from PersonajesSprites import PersonajesSprites


class Orco3(OrcoAbstracto):

    def Atacar(self):
        SpritesAtacar = []
        for i in range(0, 7):
            imagen = 'Imagenes/Orcos/Orco3/Ataque/Ataque' + str(i + 1) + '.png'
            SpritesAtacar.append(PersonajesSprites(imagen))

        return SpritesAtacar

    def Caminar(self):
        SpritesCaminar = []
        for i in range(0, 7):
            imagen = 'Imagenes/Orcos/Orco3/Caminar/Caminar' + str(i + 1) + '.png'
            SpritesCaminar.append(PersonajesSprites(imagen))

        return SpritesCaminar

    def Muerte(self):
        SpritesMuerte = []
        for i in range(0, 7):
            imagen = 'Imagenes/Orcos/Orco3/Muerte/Muerte' + str(i + 1) + '.png'
            SpritesMuerte.append(PersonajesSprites(imagen))

        return SpritesMuerte
