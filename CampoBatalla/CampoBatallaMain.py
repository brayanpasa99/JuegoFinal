import pygame
import random

from CampoBatalla import Castillos
from Jugador import Jugador
from PersonajesC import OrcoConcreto1, ElfoConcreto1, GuerreroConcreto1, OrcoConcreto2, OrcoConcreto3, ElfoConcreto2, \
    ElfoConcreto3, GuerreroConcreto2, GuerreroConcreto3

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
            pygame.display.update()

    def creaJugador(self, raza, vidaCastillo, cantOro):
        self._jugadores.append(Jugador(vidaCastillo, cantOro, raza))


    def entregaAvatar(self):
        for i in range(0, len(self._jugadores)):
            if self._jugadores[i].escogerUnidad() == 'Orco':
                self._avatares.append(OrcoConcreto1.OrcoConcreto1().SpritesAtacar()[0].image)
                self._avatares.append(OrcoConcreto2.OrcoConcreto2().SpritesAtacar()[0].image)
                self._avatares.append(OrcoConcreto3.OrcoConcreto3().SpritesAtacar()[0].image)

            elif self._jugadores[i].escogerUnidad() == 'Elfo':
                self._avatares.append(ElfoConcreto1.ElfoConcreto1().SpritesAtacar()[0].image)
                self._avatares.append(ElfoConcreto2.ElfoConcreto2().SpritesAtacar()[0].image)
                self._avatares.append(ElfoConcreto3.ElfoConcreto3().SpritesAtacar()[0].image)

            elif self._jugadores[i].escogerUnidad() == 'Guerrero':
                self._avatares.append(GuerreroConcreto1.GuerreroConcreto1().SpritesAtacar()[0].image)
                self._avatares.append(GuerreroConcreto2.GuerreroConcreto2().SpritesAtacar()[0].image)
                self._avatares.append(GuerreroConcreto3.GuerreroConcreto3().SpritesAtacar()[0].image)


