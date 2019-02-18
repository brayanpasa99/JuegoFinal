import pygame
from pygame.locals import *

class Orco1(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagenes = {'Ataque': {'Ataque1': 'Imagenes/Orcos/Orco1/Ataque/Ataque1.png', 'Ataque2': 'Imagenes/Orcos/Orco1/Ataque/Ataque2.png',
                          'Ataque3': 'Imagenes/Orcos/Orco1/Ataque/Ataque3.png', 'Ataque4': 'Imagenes/Orcos/Orco1/Ataque/Ataque4.png',
                          'Ataque5': 'Imagenes/Orcos/Orco1/Ataque/Ataque5.png', 'Ataque6': 'Imagenes/Orcos/Orco1/Ataque/Ataque6.png',
                          'Ataque7': 'Imagenes/Orcos/Orco1/Ataque/Ataque7.png'}, 'Muerte':
                         {'Muerte1': 'Imagenes/Orcos/Orco1/Muerte/Muerte1.png', 'Muerte2': 'Imagenes/Orcos/Orco1/Muerte/Muerte2.png',
                          'Muerte3': 'Imagenes/Orcos/Orco1/Muerte/Muerte3.png', 'Muerte4': 'Imagenes/Orcos/Orco1/Muerte/Muerte4.png',
                          'Muerte5': 'Imagenes/Orcos/Orco1/Muerte/Muerte5.png', 'Muerte6': 'Imagenes/Orcos/Orco1/Muerte/Muerte6.png',
                          'Muerte7': 'Imagenes/Orcos/Orco1/Muerte/Muerte7.png'}, 'Caminar':
            {'Caminar1': 'Imagenes/Orcos/Orco1/Caminar/Caminar1.png', 'Caminar2': 'Imagenes/Orcos/Orco1/Caminar/Caminar2.png',
             'Caminar3': 'Imagenes/Orcos/Orco1/Caminar/Caminar3.png', 'Caminar4': 'Imagenes/Orcos/Orco1/Caminar/Caminar4.png',
             'Caminar5': 'Imagenes/Orcos/Orco1/Caminar/Caminar5.png', 'Caminar6': 'Imagenes/Orcos/Orco1/Caminar/Caminar6.png',
             'Caminar7': 'Imagenes/Orcos/Orco1/Caminar/Caminar7.png'}}
