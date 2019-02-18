import pygame
from pygame.locals import *
import random
from CampoBatalla import Castillos
from CampoBatalla import Personajes

DIMENSIONES = (1000, 500)
COLOR_TEXTO = (243, 255, 0)
FONDOS = ['Fondo1.png', 'Fondo2.png', 'Fondo3.jpg', 'Fondo4.jpg', 'Fondo5.png']

class CampoBatallaMain():

    def main(self):

        pygame.init()

        jugando = True

        ventana = pygame.display.set_mode(DIMENSIONES)
        pygame.display.set_caption("Castillos")

        CastilloAmigo = Castillos.Castillo()
        CastilloEnemigo = Castillos.Castillo()

        image_CastilloAmigo = pygame.transform.scale(pygame.image.load('Imagenes/'+CastilloAmigo.castilloInicial()), (300, 400))
        rec_CastilloAmigo = image_CastilloAmigo.get_rect()
        rec_CastilloAmigo.topleft = (10, 10)

        image_CastilloEnemigo = pygame.transform.scale(pygame.image.load('Imagenes/'+CastilloEnemigo.castilloInicial()), (300, 400))
        rec_CastilloEnemigo = image_CastilloEnemigo.get_rect()
        rec_CastilloEnemigo.topleft = (10, 10)
        image_CastilloEnemigo = pygame.transform.flip(image_CastilloEnemigo, True, False)

        PersonajeAmigo = Personajes.Personaje().figuras()
        PersonajeEnemigo = Personajes.Personaje().figuras()

        image_PAmigo1 = pygame.transform.scale(pygame.image.load('Imagenes/'+PersonajeAmigo[0]), (50, 50))
        image_PAmigo2 = pygame.transform.scale(pygame.image.load('Imagenes/'+PersonajeAmigo[1]), (50, 50))
        image_PAmigo3 = pygame.transform.scale(pygame.image.load('Imagenes/'+PersonajeAmigo[2]), (50, 50))

        image_PEnemigo1 = pygame.transform.scale(pygame.image.load('Imagenes/'+PersonajeEnemigo[0]), (50, 50))
        image_PEnemigo2 = pygame.transform.scale(pygame.image.load('Imagenes/'+PersonajeEnemigo[1]), (50, 50))
        image_PEnemigo3 = pygame.transform.scale(pygame.image.load('Imagenes/'+PersonajeEnemigo[2]), (50, 50))

        image_Fondo = pygame.transform.scale(pygame.image.load('Imagenes/'+FONDOS[random.randrange(5)]), (1000, 500))

        while jugando:

            ventana.blit(image_Fondo, (0, 0))
            ventana.blit(image_CastilloAmigo, (800, 40))
            ventana.blit(image_CastilloEnemigo, (-100, 40))
            ventana.blit(image_PAmigo1, (200, 50))
            ventana.blit(image_PAmigo2, (260, 50))
            ventana.blit(image_PAmigo3, (320, 50))

            ventana.blit(image_PEnemigo1, (650, 50))
            ventana.blit(image_PEnemigo2, (710, 50))
            ventana.blit(image_PEnemigo3, (770, 50))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            pygame.display.update()


