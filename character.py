import pygame


class Character(pygame.sprite.Sprite):
    def __init__(self, image, position=None):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.position = position
        self.x = self.position[0]
        self.y = self.position[1]
        self.rect = self.image.get_rect()

    def update(self, delta_time):
        self.position = (self.x, self.y)
        self.rect = self.image.get_rect()
        self.rect.center = self.position
