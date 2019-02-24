from AbstractFactory.ElfoAbstracto import ElfoAbstracto
from PersonajesSprites import PersonajesSprites
import pygame
from pygame.locals import *


class Elfo2(ElfoAbstracto):

    def Atacar(self):
        SpritesAtacar = []
        for i in range(0, 5):
            imagen = 'Imagenes/Elfos/Elfo2/Ataque/Ataque' + str(i + 1) + '.png'
            SpritesAtacar.append(PersonajesSprites(imagen, (50, 50)))

        return SpritesAtacar

    def Caminar(self):
        SpritesCaminar = []
        for i in range(0, 3):
            imagen = '../Imagenes/Elfos/Elfo2/Caminar/Caminar' + str(i + 1) + '.png'
            SpritesCaminar.append(PersonajesSprites(imagen, (50, 50)))

        return SpritesCaminar

    def Muerte(self):
        SpritesMuerte = []
        for i in range(0, 5):
            imagen = '../Imagenes/Elfos/Elfo2/Muerte/Muerte' + str(i + 1) + '.png'
            SpritesMuerte.append(PersonajesSprites(imagen, (50, 50)))

        return SpritesMuerte

    def update(self):
        teclas = pygame.key.get_pressed()

        if teclas[K_s]:
            self.Atacar()[0].rect = (300, 300)

    def dibujar(self, ventana):
        ventana.blit(self.Atacar()[0].image, (240, 300))
