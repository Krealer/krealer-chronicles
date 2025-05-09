# player.py
import pygame
from settings import *

# Player class represents Krealer, the main controllable character
class Player(pygame.sprite.Sprite):
    def __init__(self, pos, scale=(100, 100)):
        super().__init__()  # Initialize the Sprite superclass

        # Load the player's image from file
        self.image = pygame.image.load("assets/images/krealer.png").convert_alpha()

        # Resize the image to the desired width and height for better fit on screen
        self.image = pygame.transform.scale(self.image, scale)

        # Get the rectangle (position and size) from the image, and set the starting position
        self.rect = self.image.get_rect(center=pos)

        # Movement speed in pixels per frame, imported from settings
        self.speed = PLAYER_SPEED

    # Handle user input for character movement
    def handle_input(self, obstacles):
        # Store the current position to roll back if collision happens
        original_position = self.rect.copy()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.speed

        # Check for collisions with any obstacles
        for obstacle in obstacles:
            if self.rect.colliderect(obstacle):
                self.rect = original_position  # Revert to previous position if colliding

    # Update function called automatically every frame
    def update(self, obstacles):
        self.handle_input(obstacles)  # Check for user input and move accordingly
