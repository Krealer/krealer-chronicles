import pygame
from settings import *

# Player class represents Krealer
class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()  # Call Sprite's constructor

        # Load the player's image (Krealer)
        self.image = pygame.image.load("assets/images/krealer.png").convert_alpha()

        # Resize if needed (optional):
        # self.image = pygame.transform.scale(self.image, (64, 64))

        # Get the rect (hitbox) from the image and set starting position
        self.rect = self.image.get_rect(center=pos)

        # Movement speed from settings
        self.speed = PLAYER_SPEED

    def handle_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.speed

    def update(self):
        self.handle_input()
