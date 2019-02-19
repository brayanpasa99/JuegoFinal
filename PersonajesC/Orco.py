import pygame
from pygame.locals import *

class OrcoSprites(pygame.sprite.Sprite):

    def __init__(self, dirImage):
        self.image = pygame.transform.scale(pygame.image.load(dirImage), (50, 50))
        self.rect = self.image.get_rect()


def ObtieneSprites():
    _TodosSprites = []
    for i in range(0, 7):
        imagen = '../Imagenes/Orcos/Orco1/Ataque/Ataque'+str(i+1)+'.png'
        _TodosSprites.append(OrcoSprites(imagen))
       
    ventana = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Castillos")

    while 1:
        for i in range(0, 7):
            ventana.blit(_TodosSprites[i].image, ((i*i*i)+50, 50))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        pygame.display.update()

if __name__ == '__main__':
    ObtieneSprites()
