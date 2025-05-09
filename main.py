import pygame
import sys
from settings import *

# Initialize all imported pygame modules
pygame.init()

# Create the main game window
# Using the WIDTH and HEIGHT from settings.py
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Krealer Chronicles")

# Clock helps us control the frame rate (FPS)
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    # 1. Handle Events (like keyboard, quit)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Exit the game loop

    # 2. Game Logic Goes Here (player movement, collision, etc.)
    # For now, we'll keep it empty until we add more

    # 3. Drawing Section
    screen.fill(BACKGROUND_COLOR)  # Fill the screen with a color

    # 4. Update the display
    pygame.display.flip()  # Or pygame.display.update()

    # 5. Tick the clock to run at desired FPS
    clock.tick(FPS)  # Limits the loop to 'FPS' times per second

# Quit pygame properly
pygame.quit()
sys.exit()
