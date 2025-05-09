import pygame
import sys
from settings import *
from player import Player

# Initialize all imported pygame modules
pygame.init()

# Create the main game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Krealer Chronicles")

# Clock helps us control the frame rate (FPS)
clock = pygame.time.Clock()

# Create a sprite group and add the player
all_sprites = pygame.sprite.Group()
player = Player((WIDTH // 2, HEIGHT // 2))  # Start in center
all_sprites.add(player)

# Main game loop
running = True
while running:
    # 1. Handle Events (like keyboard, quit)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. Update game logic
    all_sprites.update()  # This calls each sprite's update()

    # 3. Drawing section
    screen.fill(BACKGROUND_COLOR)
    all_sprites.draw(screen)  # Draw all sprites

    # 4. Update the display
    pygame.display.flip()

    # 5. Tick the clock to run at desired FPS
    clock.tick(FPS)

# Quit pygame properly
pygame.quit()
sys.exit()
