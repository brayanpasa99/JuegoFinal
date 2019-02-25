from AbstractFactory.ElfoAbstracto import ElfoAbstracto
from PersonajesSprites import PersonajesSprites
import pygame
from pygame.locals import *


class Elfo3(ElfoAbstracto):

    rect = (0, 0)

    def Atacar(self):
        SpritesAtacar = []
        for i in range(0, 5):
            imagen = 'Imagenes/Elfos/Elfo3/Ataque/Ataque' + str(i + 1) + '.png'
            SpritesAtacar.append(PersonajesSprites(imagen, (50, 50)))

        return SpritesAtacar

    def Caminar(self):
        SpritesCaminar = []
        for i in range(0, 3):
            imagen = 'Imagenes/Elfos/Elfo3/Caminar/Caminar' + str(i + 1) + '.png'
            SpritesCaminar.append(PersonajesSprites(imagen, (50, 50)))

        return SpritesCaminar

    def Muerte(self):
        SpritesMuerte = []
        for i in range(0, 5):
            imagen = 'Imagenes/Elfos/Elfo3/Muerte/Muerte' + str(i + 1) + '.png'
            SpritesMuerte.append(PersonajesSprites(imagen, (50, 50)))

        return SpritesMuerte

    def update(self):
        teclas = pygame.key.get_pressed()


    def dibujar(self, ventana):
        pass

