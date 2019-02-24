import pygame
import random

from AbstractFactory.Elfo import Elfo
from AbstractFactory.Guerrero import Guerrero
from AbstractFactory.Orco import Orco
from CampoBatalla import Castillos
from Jugador import Jugador
from pygame.locals import *

DIMENSIONES = (1000, 500)
COLOR_TEXTO = (243, 255, 0)
FONDOS = ['Fondo1.png', 'Fondo2.png', 'Fondo3.jpg', 'Fondo4.jpg', 'Fondo5.png']

class CampoBatallaMain():

    _jugadores = []
    _avatares = []

    def main(self):

        pygame.init()

        ventana = pygame.display.set_mode(DIMENSIONES)
        pygame.display.set_caption("Castillos")

        CastilloAmigo = Castillos.Castillo()
        CastilloEnemigo = Castillos.Castillo()

        image_CastilloAmigo = pygame.transform.scale(pygame.image.load('Imagenes/Castillos/'+CastilloAmigo.castilloInicial()), (300, 400))
        rec_CastilloAmigo = image_CastilloAmigo.get_rect()
        rec_CastilloAmigo.topleft = (10, 10)

        image_CastilloEnemigo = pygame.transform.scale(pygame.image.load('Imagenes/Castillos/'+CastilloEnemigo.castilloInicial()), (300, 400))
        rec_CastilloEnemigo = image_CastilloEnemigo.get_rect()
        rec_CastilloEnemigo.topleft = (10, 10)
        image_CastilloEnemigo = pygame.transform.flip(image_CastilloEnemigo, True, False)

        image_Fondo = pygame.transform.scale(pygame.image.load('Imagenes/Fondos/'+FONDOS[random.randrange(5)]), (1000, 500))

        teclas = pygame.key.get_pressed()

        while True:

            ventana.blit(image_Fondo, (0, 0))
            ventana.blit(image_CastilloAmigo, (800, 40))
            ventana.blit(image_CastilloEnemigo, (-100, 40))
            ventana.blit(self._avatares[0], (200, 50))
            ventana.blit(self._avatares[1], (280, 50))
            ventana.blit(self._avatares[2], (360, 50))

            ventana.blit(self._avatares[3], (610, 50))
            ventana.blit(self._avatares[4], (690, 50))
            ventana.blit(self._avatares[5], (770, 50))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()


            Elfo().Personaje1().dibujar(ventana)

            Elfo().Personaje1().update()

            Elfo().Personaje2().update()
            Elfo().Personaje2().dibujar(ventana)
            Elfo().Personaje3().update()
            Elfo().Personaje3().dibujar(ventana)

            pygame.display.flip()

    def creaJugador(self, raza, vidaCastillo, cantOro):
        self._jugadores.append(Jugador(vidaCastillo, cantOro, raza))


    def entregaAvatar(self):
        for i in range(0, len(self._jugadores)):
            if self._jugadores[i].escogerUnidad() == 'Orco':
                self._avatares.append(Orco().Personaje1().Atacar()[0].image)
                self._avatares.append(Orco().Personaje2().Atacar()[0].image)
                self._avatares.append(Orco().Personaje3().Atacar()[0].image)

            elif self._jugadores[i].escogerUnidad() == 'Elfo':
                self._avatares.append(Elfo().Personaje1().Atacar()[0].image)
                self._avatares.append(Elfo().Personaje2().Atacar()[0].image)
                self._avatares.append(Elfo().Personaje3().Atacar()[0].image)

            elif self._jugadores[i].escogerUnidad() == 'Guerrero':
                self._avatares.append(Guerrero().Personaje1().Atacar()[0].image)
                self._avatares.append(Guerrero().Personaje2().Atacar()[0].image)
                self._avatares.append(Guerrero().Personaje3().Atacar()[0].image)


