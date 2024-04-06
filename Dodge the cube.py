import pygame
import random
import sys

pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dodger")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

player_size = 50
player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT - 2 * player_size]
player_speed = 10

obstacle_size = 50
obstacle_pos = [random.randint(0, SCREEN_WIDTH - obstacle_size), 0]
obstacle_list = [obstacle_pos]
obstacle_speed = 5

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < SCREEN_WIDTH - player_size:
        player_pos[0] += player_speed

    for idx, obstacle in enumerate(obstacle_list):
        obstacle[1] += obstacle_speed
        if obstacle[1] > SCREEN_HEIGHT:
            obstacle_list.pop(idx)
            obstacle_list.append([random.randint(0, SCREEN_WIDTH - obstacle_size), 0])

    for obstacle in obstacle_list:
        if obstacle[1] + obstacle_size > player_pos[1] and player_pos[0] < obstacle[0] + obstacle_size and player_pos[0] + player_size > obstacle[0]:
            pygame.quit()
            sys.exit()

    screen.fill(WHITE)

    pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))

    for obstacle in obstacle_list:
        pygame.draw.rect(screen, RED, (obstacle[0], obstacle[1], obstacle_size, obstacle_size))

    pygame.display.update()

    clock.tick(30)
