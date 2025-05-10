# thornsoul.py
import pygame

class Thornsoul(pygame.sprite.Sprite):
    def __init__(self, pos, scale=(100, 100)):
        super().__init__()
        self.image = pygame.image.load("assets/images/thornsoul.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, scale)
        self.rect = self.image.get_rect(center=pos)

    def update(self, *args, **kwargs):
        pass  # No behavior yet, but accepts arguments to avoid update errors
