from AbstractFactory.ElfoAbstracto import ElfoAbstracto
from PersonajesSprites import PersonajesSprites


class Elfo2(ElfoAbstracto):

    def Atacar(self):
        SpritesAtacar = []
        for i in range(0, 5):
            imagen = 'Imagenes/Elfos/Elfo2/Ataque/Ataque' + str(i + 1) + '.png'
            SpritesAtacar.append(PersonajesSprites(imagen))

        return SpritesAtacar

    def Caminar(self):
        SpritesCaminar = []
        for i in range(0, 3):
            imagen = '../Imagenes/Elfos/Elfo2/Caminar/Caminar' + str(i + 1) + '.png'
            SpritesCaminar.append(PersonajesSprites(imagen))

        return SpritesCaminar

    def Muerte(self):
        SpritesMuerte = []
        for i in range(0, 5):
            imagen = '../Imagenes/Elfos/Elfo2/Muerte/Muerte' + str(i + 1) + '.png'
            SpritesMuerte.append(PersonajesSprites(imagen))

        return SpritesMuerte
