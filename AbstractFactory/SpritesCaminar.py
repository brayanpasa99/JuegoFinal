from AbstractFactory.Sprites import Sprites


class SpritesCaminar(Sprites):

    def spritesElfo(self):
        return SpritesCaminarElfo()

    def spritesGuerrero(self):
        return SpritesCaminarGuerrero()

    def spritesOrco(self):
        return SpritesCaminarOrco()
