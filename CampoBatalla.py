import pygame
from pygame.locals import *

DIMENSIONES = (650, 500)
COLOR_TEXTO = (243, 255, 0)

class CampoBatalla():

    def castillos(self):
        pygame.init()

        jugando = True

        ventana = pygame.display.set_mode(DIMENSIONES)
        pygame.display.set_caption("Castillos")

        while jugando:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            pygame.display.update()


