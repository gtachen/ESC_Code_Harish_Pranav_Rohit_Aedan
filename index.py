### Test this in trinkets. idk how to test it on github codespaces
### If you test in trinkets, make sure to upload the image files to the trinket 
### I couldn't find any images that fit so it looks very mediocre
### I did use AI

import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen settings
WIDTH = 900
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load images
player_img = pygame.image.load('astro (2).png')  
enemy_img = pygame.image.load('Rock.png')


# Game variables
player_x = WIDTH // 2 - 32
player_y = HEIGHT - 80
player_speed = 5

enemies = []
enemy_speed = 10
spawn_delay = 30 # Interval for spawning enemies
spawn_timer = 0

clock = pygame.time.Clock()

# Game loop
running = True
while running:
    clock.tick(60)
    screen.fill(BLACK)

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - 64:
        player_x += player_speed


    # Spawn enemies
    spawn_timer += 1
    if spawn_timer >= spawn_delay:
        x = random.randint(0, WIDTH - 64)
        enemies.append([x, -64])
        spawn_timer = 0

    # Update enemies
    for e in enemies[:]:
        e[1] += enemy_speed
        if e[1] > HEIGHT:
            enemies.remove(e)
            
    # Check Collisions: Player and Asteriod
    player_rect = pygame.Rect(player_x, player_y, 32, 32)
    for e in enemies:
      enemy_rect = pygame.Rect(e[0], e[1], 100, 100)
      if player_rect.colliderect(enemy_rect):
        running = False

    # Draw everything
    screen.blit(player_img, (player_x, player_y))
    for e in enemies:
        screen.blit(enemy_img, (e[0], e[1]))

    pygame.display.flip()

    # Quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()

