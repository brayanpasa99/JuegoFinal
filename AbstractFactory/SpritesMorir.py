from AbstractFactory.Sprites import Sprites


class SpritesMorir(Sprites):

    def spritesElfo(self):
        return SpritesMorirElfo()

    def spritesGuerrero(self):
        return SpritesMorirGuerrero()

    def spritesOrco(self):
        return SpritesMorirOrco()
