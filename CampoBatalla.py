import pygame
from pygame.locals import *

DIMENSIONES = (1000, 500)
COLOR_TEXTO = (243, 255, 0)

class CampoBatalla():

    __personajes = None

    def figuras(self, personajes):
        self.__personajes = personajes

    def castillos(self):
        pygame.init()

        jugando = True

        ventana = pygame.display.set_mode(DIMENSIONES)
        pygame.display.set_caption("Castillos")

        image_CastilloVerde = pygame.transform.scale(pygame.image.load('Imagenes/CastilloVerde.png'), (300, 400))
        rec_CastilloVerde = image_CastilloVerde.get_rect()
        rec_CastilloVerde.topleft = (10, 10)

        image_CastilloBlanco = pygame.transform.scale(pygame.image.load('Imagenes/CastilloBlanco.png'), (300, 400))
        rec_CastilloBlanco = image_CastilloBlanco.get_rect()
        rec_CastilloBlanco.topleft = (10, 10)
        image_CastilloBlanco = pygame.transform.flip(image_CastilloBlanco, True, False)

        image_Fondo = pygame.transform.scale(pygame.image.load('Imagenes/Fondo2.jpg'), (1000, 500))

        pasarper = ['Orco1.png', 'Orco2.png', 'Orco3.png']
        self.figuras(pasarper)
        str_personaje1 = self.__personajes[0]
        str_personaje2 = self.__personajes[1]
        str_personaje3 = self.__personajes[2]

        imagen_personaje1 = pygame.image.load('Imagenes/'+str_personaje1)
        imagen_personaje2 = pygame.image.load('Imagenes/'+str_personaje2)
        imagen_personaje3 = pygame.image.load('Imagenes/'+str_personaje3)

        while jugando:

            ventana.blit(image_Fondo, (0, 0))
            ventana.blit(image_CastilloVerde, (800, 40))
            ventana.blit(image_CastilloBlanco, (-100, 40))
            ventana.blit(imagen_personaje1, (50, 50))
            ventana.blit(imagen_personaje2, (100, 50))
            ventana.blit(imagen_personaje3, (150, 50))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            pygame.display.update()


