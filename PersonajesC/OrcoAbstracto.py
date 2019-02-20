import abc
import pygame

class OrcosSprites():

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def SpritesAtacar(self):
        pass

    @abc.abstractmethod
    def SpritesCaminar(self):
        pass

    @abc.abstractmethod
    def SpritesMuerte(self):
        pass

    @abc.abstractmethod
    def getSpritesAracar(self):
        pass

    @abc.abstractmethod
    def getSpritesCaminar(self):
        pass

    @abc.abstractmethod
    def getSpritesMatar(self):
        pass

'''import pygame
from pygame.locals import *

class OrcoSprites(pygame.sprite.Sprite):

    def __init__(self, dirImage):
        self.image = pygame.transform.scale(pygame.image.load(dirImage), (50, 50))
        self.rect = self.image.get_rect()


def SpritesAtacar():
        _SpritesAtaque = []
        imagen = ''
        for i in range(0, 7):
            imagen = '../Imagenes/Orcos/Orco1/Ataque/Ataque'+str(i+1)+'.png'
            _SpritesAtaque.append(OrcoSprites(imagen))

        ventana = pygame.display.set_mode((500, 500))
        pygame.display.set_caption("Castillos")

        while 1:
            for i in range(0, 7):
                ventana.blit(_SpritesAtaque[i].image, ((i*i*i)+50, 50))


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            pygame.display.update()

if __name__ == '__main__':
    SpritesAtacar()'''
