import pygame
import random

from Jugador import Jugador
from pygame.locals import *

DIMENSIONES = (1000, 500)
COLOR_TEXTO = (243, 255, 0)
FONDOS = ['Fondo1.png', 'Fondo2.png', 'Fondo3.jpg', 'Fondo4.jpg', 'Fondo5.png']

class CampoBatallaMain():

    def main(self, jugadores):

        pygame.init()

        ventana = pygame.display.set_mode(DIMENSIONES)
        pygame.display.set_caption("Campo de Batalla")

        image_CastilloAmigo = jugadores[0].Personaje1.castillo[0].image
        image_CastilloAmigo = pygame.transform.flip(image_CastilloAmigo, True, False)
        image_CastilloEnemigo = jugadores[1].Personaje1.castillo[0].image

        image_Fondo = pygame.transform.scale(pygame.image.load('Imagenes/Fondos/'+FONDOS[random.randrange(5)]), (1000, 500))

        teclas = pygame.key.get_pressed()

        while True:

            ventana.blit(image_Fondo, (0, 0))
            ventana.blit(image_CastilloAmigo, (-100, 40))
            ventana.blit(image_CastilloEnemigo, (800, 40))
            x1 = 200
            for i in range(0, 3):
                pass
#                ventana.blit(pygame.transform.scale((jugadores[0].iconos[i].image), (50, 50)), (x1, 50))
#               x1+=80

            x2 = 610
            for i in range(0,3):
                pass
#                ventana.blit(pygame.transform.scale((jugadores[1].iconos[i].image), (50, 50)), (x2, 50))
#                x2+=80

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            pygame.display.flip()

