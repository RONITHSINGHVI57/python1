import math
import random
import pygame

# Constants
screen_width = 800
screen_height = 500
player_start_x = 370
player_start_y = 380
enemy_start_y_min = 50
enemy_start_y_max = 150
enemy_speed_x = 4
enemy_speed_y = 10
collision_distance = 27

# Initialize Pygame
pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.image.load('background.png')
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
playerx = player_start_x
playery = player_start_y
playerx_change = 0

# Enemy
enemy_image = []
enemyx = []
enemyy = []
enemyx_change = []
enemyy_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemy_image.append(pygame.image.load('enemy.png'))
    enemyx.append(random.randint(0, screen_width - 64))
    enemyy.append(random.randint(enemy_start_y_min, enemy_start_y_max))
    enemyx_change.append(enemy_speed_x)
    enemyy_change.append(enemy_speed_y)

# Bullet
bulletImg = pygame.image.load('bullet.png')
bulletx = 0
bullety = playery
bullety_change = 10
bullet_state = "ready"  # "ready" - You can't see the bullet, "fire" - bullet is moving

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textx = 10
texty = 10

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemy_image[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt((enemy_x - bullet_x) ** 2 + (enemy_y - bullet_y) ** 2)
    return distance < collision_distance


# Game Loop
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Key press
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_change = -5
            if event.key == pygame.K_RIGHT:
                playerx_change = 5
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bulletx = playerx
                fire_bullet(bulletx, bullety)

        # Key release
        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                playerx_change = 0

    # Player Movement
    playerx += playerx_change
    playerx = max(0, min(playerx, screen_width - 64))  # Player boundaries

    # Enemy Movement
    for i in range(num_of_enemies):
        if enemyy[i] > 340:
            for j in range(num_of_enemies):
                enemyy[j] = 2000
            game_over_text()
            break

        enemyx[i] += enemyx_change[i]
        if enemyx[i] <= 0 or enemyx[i] >= screen_width - 64:
            enemyx_change[i] *= -1
            enemyy[i] += enemyy_change[i]

        # Collision
        if is_collision(enemyx[i], enemyy[i], bulletx, bullety):
            bullety = playery
            bullet_state = "ready"
            score_value += 1
            enemyx[i] = random.randint(0, screen_width - 64)
            enemyy[i] = random.randint(enemy_start_y_min, enemy_start_y_max)

        enemy(enemyx[i], enemyy[i], i)

    # Bullet Movement
    if bullet_state == "fire":
        fire_bullet(bulletx, bullety)
        bullety -= bullety_change

    if bullety <= 0:
        bullety = playery
        bullet_state = "ready"

    player(playerx, playery)
    show_score(textx, texty)
    pygame.display.update()
