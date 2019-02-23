import abc


class Sprites():
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def spritesElfo(self):
        pass

    @abc.abstractmethod
    def spritesGuerrero(self):
        pass

    @abc.abstractmethod
    def spritesOrco(self):
        pass
