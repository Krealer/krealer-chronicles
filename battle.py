# battle.py
import pygame
import random
from settings import *

def start_battle(screen):
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 36)

    # Load and scale Krealer and Thornsoul images
    krealer_img = pygame.image.load("assets/images/krealer.png").convert_alpha()
    krealer_img = pygame.transform.scale(krealer_img, (500, 500))

    thornsoul_img = pygame.image.load("assets/images/thornsoul.png").convert_alpha()
    thornsoul_img = pygame.transform.scale(thornsoul_img, (500, 500))

    # Set initial HP for both characters
    player_hp = 5000
    boss_hp = 10000
    max_player_hp = 5000
    max_boss_hp = 10000

    # Battle state control
    turn = "player"  # Tracks whose turn it is
    running = True
    skill_message = ""
    wait_for_space = False  # Controls message delay between turns

    # Special ability states
    thornsoul_used_recovery = False  # Limits Thorn Recovery to one use
    reflect_next_hit = False         # Triggers reflection of Krealer's next attack
    disable_krealer_heal = False     # Blocks Krealer's heal once
    krealer_up_points = 0            # Tracks UP! points for Storm of Code

    while running:
        screen.fill(BLACK)

        # Handle user input and events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if wait_for_space and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                wait_for_space = False

            if not wait_for_space and turn == "player" and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    # Skill 1: !?!?
                    damage = random.randint(400, 500)
                    if reflect_next_hit:
                        player_hp -= int(damage * 0.5)
                        skill_message = f"Krealer used !?!? Reflected! (-{int(damage*0.5)})"
                        reflect_next_hit = False
                    boss_hp -= damage
                    skill_message = f"Krealer used !?!? (-{damage})"
                    turn = "boss"
                    wait_for_space = True

                elif event.key == pygame.K_2:
                    # Skill 2: Absorb
                    damage = random.randint(300, 400)
                    if reflect_next_hit:
                        player_hp -= int(damage * 0.5)
                        skill_message = f"Krealer used Absorb but it was reflected! (-{int(damage*0.5)})"
                        reflect_next_hit = False
                    else:
                        boss_hp -= damage
                        player_hp += damage
                        player_hp = min(player_hp, max_player_hp)
                        skill_message = f"Krealer used Absorb! (-{damage}, +{damage})"
                    turn = "boss"
                    wait_for_space = True

                elif event.key == pygame.K_3:
                    # Skill 3: UP!
                    krealer_up_points += 1
                    skill_message = f"Krealer used UP! (UP Points: {krealer_up_points})"
                    turn = "boss"
                    wait_for_space = True

                elif event.key == pygame.K_4:
                    # Skill 4: Storm of Code
                    if krealer_up_points > 0:
                        damage = krealer_up_points * 500
                        boss_hp -= damage
                        skill_message = f"Krealer used Storm of Code! (-{damage})"
                        krealer_up_points = 0
                    else:
                        skill_message = "Not enough UP points to use Storm of Code!"
                    turn = "boss"
                    wait_for_space = True

            elif not wait_for_space and turn == "boss":
                # Boss chooses and performs a skill
                pygame.time.delay(500)
                available_skills = []
                if boss_hp < max_boss_hp * 0.4:
                    available_skills += ["dark_soul", "dark_thorns"]
                if boss_hp < max_boss_hp * 0.5 and not thornsoul_used_recovery:
                    available_skills.append("thorn_recovery")
                available_skills += ["prickle_thorns", "thorn_defence"]

                skill = random.choice(available_skills)
                if skill == "prickle_thorns":
                    damage = random.randint(300, 400)
                    player_hp -= damage
                    skill_message = f"Thornsoul used Prickle Thorns! (-{damage})"
                elif skill == "thorn_defence":
                    reflect_next_hit = True
                    skill_message = "Thornsoul used Thorn Defence! Reflecting next hit."
                elif skill == "thorn_recovery":
                    heal = 3000
                    boss_hp += heal
                    boss_hp = min(boss_hp, max_boss_hp)
                    reflect_next_hit = True
                    thornsoul_used_recovery = True
                    skill_message = "Thornsoul used Thorn Recovery! (+3000 & reflect)"
                elif skill == "dark_soul":
                    damage = random.randint(100, 300)
                    player_hp -= damage
                    disable_krealer_heal = True
                    skill_message = f"Thornsoul used Dark Soul! (-{damage}, heal blocked)"
                elif skill == "dark_thorns":
                    damage = random.randint(300, 600)
                    player_hp -= damage
                    skill_message = f"Thornsoul used Dark Thorns! (-{damage})"
                turn = "player"
                wait_for_space = True

        # Character positions
        krealer_x = WIDTH - 900
        thornsoul_x = WIDTH - 400
        character_y = HEIGHT // 2 - 200

        # Health bar sizes
        krealer_bar_width = int((player_hp / max_player_hp) * 200)
        thornsoul_bar_width = int((boss_hp / max_boss_hp) * 200)

        # Center bars above sprites
        krealer_bar_x = krealer_x + 250 - krealer_bar_width // 2
        thornsoul_bar_x = thornsoul_x + 250 - thornsoul_bar_width // 2

        # Draw sprites and UI elements
        screen.blit(krealer_img, (krealer_x, character_y))
        screen.blit(thornsoul_img, (thornsoul_x, character_y))

        pygame.draw.rect(screen, RED, (krealer_bar_x, character_y - 40, krealer_bar_width, 25))
        pygame.draw.rect(screen, BLUE, (thornsoul_bar_x, character_y - 40, thornsoul_bar_width, 25))

        screen.blit(font.render("Krealer HP", True, WHITE), (krealer_bar_x, character_y - 70))
        screen.blit(font.render("Thornsoul HP", True, WHITE), (thornsoul_bar_x, character_y - 70))
        screen.blit(font.render(f"UP: {krealer_up_points}", True, WHITE), (50, 50))

        if wait_for_space:
            screen.blit(font.render(skill_message, True, WHITE), (50, 550))
            screen.blit(font.render("Press [SPACE] for next action", True, WHITE), (50, 600))

        pygame.display.flip()
        clock.tick(FPS)

        # Win/Lose check
        if player_hp <= 0:
            print("Krealer was defeated...")
            running = False
        elif boss_hp <= 0:
            print("Thornsoul was defeated!")
            running = False
