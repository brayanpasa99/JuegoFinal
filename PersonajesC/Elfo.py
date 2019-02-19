import pygame
from pygame.locals import *

class Elfo(pygame.sprite.Sprite):

    _imagenes = None

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self._imagenes = {'Elfo1': {'Ataque': {'Ataque1': 'Imagenes/Elfos/Elfo1/Ataque/Ataque1.png', 'Ataque2': 'Imagenes/Elfos/Elfo1/Ataque/Ataque2.png',
                          'Ataque3': 'Imagenes/Elfos/Elfo1/Ataque/Ataque3.png', 'Ataque4': 'Imagenes/Elfos/Elfo1/Ataque/Ataque4.png',
                          'Ataque5': 'Imagenes/Elfos/Elfo1/Ataque/Ataque5.png', 'Ataque6': 'Imagenes/Elfos/Elfo1/Ataque/Ataque6.png',
                          'Ataque7': 'Imagenes/Elfos/Elfo1/Ataque/Ataque7.png'}, 'Muerte':
                         {'Muerte1': 'Imagenes/Elfos/Elfo1/Muerte/Muerte1.png', 'Muerte2': 'Imagenes/Elfos/Elfo1/Muerte/Muerte2.png',
                          'Muerte3': 'Imagenes/Elfos/Elfo1/Muerte/Muerte3.png', 'Muerte4': 'Imagenes/Elfos/Elfo1/Muerte/Muerte4.png',
                          'Muerte5': 'Imagenes/Elfos/Elfo1/Muerte/Muerte5.png', 'Muerte6': 'Imagenes/Elfos/Elfo1/Muerte/Muerte6.png',
                          'Muerte7': 'Imagenes/Elfos/Elfo1/Muerte/Muerte7.png'}, 'Caminar':
            {'Caminar1': 'Imagenes/Elfos/Elfo1/Caminar/Caminar1.png', 'Caminar2': 'Imagenes/Elfos/Elfo1/Caminar/Caminar2.png',
             'Caminar3': 'Imagenes/Elfos/Elfo1/Caminar/Caminar3.png', 'Caminar4': 'Imagenes/Elfos/Elfo1/Caminar/Caminar4.png',
             'Caminar5': 'Imagenes/Elfos/Elfo1/Caminar/Caminar5.png', 'Caminar6': 'Imagenes/Elfos/Elfo1/Caminar/Caminar6.png',
             'Caminar7': 'Imagenes/Elfos/Elfo1/Caminar/Caminar7.png'}},

                          'Elfo2': {'Ataque': {'Ataque1': 'Imagenes/Elfos/Elfo2/Ataque/Ataque1.png', 'Ataque2': 'Imagenes/Elfos/Elfo2/Ataque/Ataque2.png',
                          'Ataque3': 'Imagenes/Elfos/Elfo2/Ataque/Ataque3.png', 'Ataque4': 'Imagenes/Elfos/Elfo2/Ataque/Ataque4.png',
                          'Ataque5': 'Imagenes/Elfos/Elfo2/Ataque/Ataque5.png', 'Ataque6': 'Imagenes/Elfos/Elfo2/Ataque/Ataque6.png',
                          'Ataque7': 'Imagenes/Elfos/Elfo2/Ataque/Ataque7.png'}, 'Muerte':
                         {'Muerte1': 'Imagenes/Elfos/Elfo2/Muerte/Muerte1.png', 'Muerte2': 'Imagenes/Elfos/Elfo2/Muerte/Muerte2.png',
                          'Muerte3': 'Imagenes/Elfos/Elfo2/Muerte/Muerte3.png', 'Muerte4': 'Imagenes/Elfos/Elfo2/Muerte/Muerte4.png',
                          'Muerte5': 'Imagenes/Elfos/Elfo2/Muerte/Muerte5.png', 'Muerte6': 'Imagenes/Elfos/Elfo2/Muerte/Muerte6.png',
                          'Muerte7': 'Imagenes/Elfos/Elfo2/Muerte/Muerte7.png'}, 'Caminar':
            {'Caminar1': 'Imagenes/Elfos/Elfo2/Caminar/Caminar1.png', 'Caminar2': 'Imagenes/Elfos/Elfo2/Caminar/Caminar2.png',
             'Caminar3': 'Imagenes/Elfos/Elfo2/Caminar/Caminar3.png', 'Caminar4': 'Imagenes/Elfos/Elfo2/Caminar/Caminar4.png',
             'Caminar5': 'Imagenes/Elfos/Elfo2/Caminar/Caminar5.png', 'Caminar6': 'Imagenes/Elfos/Elfo2/Caminar/Caminar6.png',
             'Caminar7': 'Imagenes/Elfos/Elfo2/Caminar/Caminar7.png'}},


                          'Elfo3': {'Ataque': {'Ataque1': 'Imagenes/Elfos/Elfo3/Ataque/Ataque1.png', 'Ataque2': 'Imagenes/Elfos/Elfo3/Ataque/Ataque2.png',
                          'Ataque3': 'Imagenes/Elfos/Elfo3/Ataque/Ataque3.png', 'Ataque4': 'Imagenes/Elfos/Elfo3/Ataque/Ataque4.png',
                          'Ataque5': 'Imagenes/Elfos/Elfo3/Ataque/Ataque5.png', 'Ataque6': 'Imagenes/Elfos/Elfo3/Ataque/Ataque6.png',
                          'Ataque7': 'Imagenes/Elfos/Elfo3/Ataque/Ataque7.png'}, 'Muerte':
                         {'Muerte1': 'Imagenes/Elfos/Elfo3/Muerte/Muerte1.png', 'Muerte2': 'Imagenes/Elfos/Elfo3/Muerte/Muerte2.png',
                          'Muerte3': 'Imagenes/Elfos/Elfo3/Muerte/Muerte3.png', 'Muerte4': 'Imagenes/Elfos/Elfo3/Muerte/Muerte4.png',
                          'Muerte5': 'Imagenes/Elfos/Elfo3/Muerte/Muerte5.png', 'Muerte6': 'Imagenes/Elfos/Elfo3/Muerte/Muerte6.png',
                          'Muerte7': 'Imagenes/Elfos/Elfo3/Muerte/Muerte7.png'}, 'Caminar':
            {'Caminar1': 'Imagenes/Elfos/Elfo3/Caminar/Caminar1.png', 'Caminar2': 'Imagenes/Elfos/Elfo3/Caminar/Caminar2.png',
             'Caminar3': 'Imagenes/Elfos/Elfo3/Caminar/Caminar3.png', 'Caminar4': 'Imagenes/Elfos/Elfo3/Caminar/Caminar4.png',
             'Caminar5': 'Imagenes/Elfos/Elfo3/Caminar/Caminar5.png', 'Caminar6': 'Imagenes/Elfos/Elfo3/Caminar/Caminar6.png',
             'Caminar7': 'Imagenes/Elfos/Elfo3/Caminar/Caminar7.png'}}}



    def entregaSprites(self, personaje):
        return self._imagenes[personaje]
