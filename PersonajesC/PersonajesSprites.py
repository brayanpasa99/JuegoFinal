import pygame

class PersonajesSprites(pygame.sprite.Sprite):

    def __init__(self, dirImage):
        self.image = pygame.transform.scale(pygame.image.load(dirImage), (70, 50))
        self.rect = self.image.get_rect()
