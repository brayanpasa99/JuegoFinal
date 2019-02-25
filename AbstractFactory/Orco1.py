from AbstractFactory.OrcoAbstracto import OrcoAbstracto
from PersonajesSprites import PersonajesSprites


class Orco1(OrcoAbstracto):

    def Atacar(self):
        SpritesAtacar = []
        for i in range(0, 7):
            imagen = 'Imagenes/Orcos/Orco1/Ataque/Ataque' + str(i + 1) + '.png'
            SpritesAtacar.append(PersonajesSprites(imagen, (50, 50)))

        return SpritesAtacar

    def Caminar(self):
        SpritesCaminar = []
        for i in range(0, 7):
            imagen = 'Imagenes/Orcos/Orco1/Caminar/Caminar' + str(i + 1) + '.png'
            SpritesCaminar.append(PersonajesSprites(imagen, (50, 50)))

        return SpritesCaminar

    def Muerte(self):
        SpritesMuerte = []
        for i in range(0, 7):
            imagen = 'Imagenes/Orcos/Orco1/Muerte/Muerte' + str(i + 1) + '.png'
            SpritesMuerte.append(PersonajesSprites(imagen, (50, 50)))

        return SpritesMuerte

