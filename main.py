# main.py
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
player = Player((WIDTH // 2, HEIGHT // 2), scale=(100, 100))  # Start in center
all_sprites.add(player)

# Define obstacle(s) as rectangles
obstacles = [
    pygame.Rect(300, 200, 200, 50),  # Example wall
    pygame.Rect(100, 400, 50, 150)   # Another wall
]

# Main game loop
running = True
while running:
    # 1. Handle Events (like keyboard, quit)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. Update game logic
    all_sprites.update(obstacles)  # Pass obstacles to the player

    # Enforce screen boundaries for the player
    if player.rect.left < 0:
        player.rect.left = 0
    if player.rect.right > WIDTH:
        player.rect.right = WIDTH
    if player.rect.top < 0:
        player.rect.top = 0
    if player.rect.bottom > HEIGHT:
        player.rect.bottom = HEIGHT

    # 3. Drawing section
    screen.fill(BACKGROUND_COLOR)

    # Draw obstacles as filled rectangles (temporary visuals)
    for obstacle in obstacles:
        pygame.draw.rect(screen, RED, obstacle)

    # Draw all sprites (player, etc.)
    all_sprites.draw(screen)

    # 4. Update the display
    pygame.display.flip()

    # 5. Tick the clock to run at desired FPS
    clock.tick(FPS)

# Quit pygame properly
pygame.quit()
sys.exit()
