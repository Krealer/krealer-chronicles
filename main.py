# main.py
import pygame
import sys
from settings import *
from player import Player
from thornsoul import Thornsoul
from battle import start_battle

# Initialize all imported pygame modules
pygame.init()

# Create the main game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Krealer Chronicles")

# Clock helps us control the frame rate (FPS)
clock = pygame.time.Clock()

# === LEVEL SETUP ===
current_level = 1
obstacles = []
goal = None
wall_color = RED
goal_color = GREEN
player = None
thornsoul = None
all_sprites = pygame.sprite.Group()

# Function to load a specific level
def load_level(level):
    global obstacles, goal, player, thornsoul, all_sprites, wall_color, goal_color
    all_sprites.empty()
    obstacles = []
    goal = None
    thornsoul = None

    if level == 1:
        wall_color = RED
        goal_color = GREEN
        player = Player((70, HEIGHT - 70), scale=(50, 50))
        all_sprites.add(player)
        obstacles.extend([
            pygame.Rect(0, 0, WIDTH, 20),
            pygame.Rect(0, HEIGHT - 20, WIDTH, 20),
            pygame.Rect(0, 0, 20, HEIGHT),
            pygame.Rect(WIDTH - 20, 0, 20, HEIGHT),
            pygame.Rect(100, 100, 600, 20),
            pygame.Rect(100, 100, 20, 400),
            pygame.Rect(200, 200, 400, 20),
            pygame.Rect(580, 200, 20, 250),
            pygame.Rect(300, 300, 300, 20),
            pygame.Rect(300, 320, 20, 150),
            pygame.Rect(400, 450, 200, 20),
        ])
        goal = pygame.Rect(WIDTH - 80, 40, 40, 40)

    elif level == 2:
        wall_color = GREEN
        goal_color = BLUE
        player = Player((40, HEIGHT - 40), scale=(20, 20))
        all_sprites.add(player)
        obstacles.extend([
            pygame.Rect(0, 0, WIDTH, 15),
            pygame.Rect(0, HEIGHT - 15, WIDTH, 15),
            pygame.Rect(0, 0, 15, HEIGHT),
            pygame.Rect(WIDTH - 15, 0, 15, HEIGHT),
            pygame.Rect(60, 60, 700, 15),
            pygame.Rect(60, 60, 15, 480),
            pygame.Rect(120, 150, 550, 15),
            pygame.Rect(650, 150, 15, 300),
            pygame.Rect(250, 250, 400, 15),
            pygame.Rect(250, 265, 15, 200),
            pygame.Rect(350, 420, 300, 15),
            pygame.Rect(150, 350, 300, 15),
            pygame.Rect(500, 350, 15, 100),
            pygame.Rect(180, 480, 500, 15),
        ])
        goal = pygame.Rect(WIDTH - 60, 30, 30, 30)

    elif level == 3:
        wall_color = BLUE
        goal_color = WHITE
        player = Player((50, HEIGHT - 50), scale=(15, 15))
        all_sprites.add(player)
        obstacles.extend([
            pygame.Rect(0, 0, WIDTH, 10),
            pygame.Rect(0, HEIGHT - 10, WIDTH, 10),
            pygame.Rect(0, 0, 10, HEIGHT),
            pygame.Rect(WIDTH - 10, 0, 10, HEIGHT),
            pygame.Rect(100, 100, 600, 10),
            pygame.Rect(100, 100, 10, 400),
            pygame.Rect(200, 150, 500, 10),
            pygame.Rect(690, 150, 10, 300),
            pygame.Rect(300, 220, 400, 10),
            pygame.Rect(300, 230, 10, 250),
            pygame.Rect(450, 480, 300, 10),
            pygame.Rect(200, 360, 400, 10),
            pygame.Rect(580, 360, 10, 80),
            pygame.Rect(120, 420, 520, 10),
        ])
        goal = pygame.Rect(WIDTH - 50, 30, 25, 25)

    elif level == 4:
        wall_color = WHITE
        player = Player((100, HEIGHT // 2), scale=(100, 100))
        thornsoul = Thornsoul((WIDTH - 150, HEIGHT // 2), scale=(100, 100))
        all_sprites.add(player)
        all_sprites.add(thornsoul)
        obstacles.extend([
            pygame.Rect(0, 0, WIDTH, 20),
            pygame.Rect(0, HEIGHT - 20, WIDTH, 20),
            pygame.Rect(0, 0, 20, HEIGHT),
            pygame.Rect(WIDTH - 20, 0, 20, HEIGHT),
        ])

# Load the initial level
load_level(current_level)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update(obstacles)

    if player.rect.left < 0:
        player.rect.left = 0
    if player.rect.right > WIDTH:
        player.rect.right = WIDTH
    if player.rect.top < 0:
        player.rect.top = 0
    if player.rect.bottom > HEIGHT:
        player.rect.bottom = HEIGHT

    if goal and player.rect.colliderect(goal):
        if current_level == 1:
            current_level = 2
            load_level(current_level)
        elif current_level == 2:
            current_level = 3
            load_level(current_level)
        elif current_level == 3:
            current_level = 4
            load_level(current_level)
        else:
            print("🎉 All levels complete!")
            running = False

    if thornsoul and player.rect.colliderect(thornsoul.rect):
        print("⚔️ Entering turn-based battle with Thornsoul!")
        start_battle(screen)
        running = False

    screen.fill(BACKGROUND_COLOR)
    if goal:
        pygame.draw.rect(screen, goal_color, goal)
    for obstacle in obstacles:
        pygame.draw.rect(screen, wall_color, obstacle)
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
