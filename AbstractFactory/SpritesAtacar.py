from AbstractFactory.Sprites import Sprites
from AbstractFactory.SpritesAtacarElfo1 import SpritesAtacarElfo1
from AbstractFactory.SpritesAtacarGuerrero1 import SpritesAtacarGuerrero1
from AbstractFactory.SpritesAtacarOrco1 import SpritesAtacarOrco1


class SpritesAtacar(Sprites):

    def spritesElfo(self):
        return SpritesAtacarElfo1()

    def spritesGuerrero(self):
        return SpritesAtacarGuerrero1()

    def spritesOrco(self):
        return SpritesAtacarOrco1()
