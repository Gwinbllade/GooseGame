import pygame
from pygame.constants import QUIT

pygame.init()

HEIGHT = 800
WIDTH = 1200

FPS = pygame.time.Clock()

COLOR_WITHE = (255, 255, 255)
BLACK  = (0,0,0)


main_display = pygame.display.set_mode((WIDTH, HEIGHT))

player_size = (20, 20)
player = pygame.Surface(player_size)
player.fill(COLOR_WITHE)
player_speed = [1, 1]

player_rect = player.get_rect()

playing = True

while playing:
    FPS.tick(120)
    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False
    
    main_display.fill(BLACK)

    if player_rect.bottom >= HEIGHT or player_rect.top < 0:
        player_speed[1] = -player_speed[1]

    if player_rect.right >= WIDTH or player_rect.left < 0:
        player_speed[0] = -player_speed[0]
    
    main_display.blit(player, player_rect)

    player_rect = player_rect.move(player_speed)
    pygame.display.flip()