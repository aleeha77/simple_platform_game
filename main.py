import pygame
from player import Player
from platform_1 import Platform
import config  

pygame.init()
screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
clock = pygame.time.Clock()

background = pygame.image.load(config.BACKGROUND_IMAGE)
background_width, background_height = background.get_size()

scroll_x = 0

player = Player()

platform1 = Platform(0, 550, 800, 20)
platform2 = Platform(100, 450, 100, 20)
platform3 = Platform(300, 350, 100, 20)
platform4 = Platform(500, 250, 100, 20)
platform5 = Platform(700, 150, 100, 20)

platforms = [platform1, platform2, platform3, platform4, platform5]

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    scroll_x -= config.BACKGROUND_SCROLL_SPEED
    if scroll_x <= -background_width:
        scroll_x = 0

    screen.blit(background, (scroll_x, 0))
    screen.blit(background, (scroll_x + background_width, 0))

    for platform in platforms:
        platform.draw(screen)

    player.update(keys, screen, platforms)

    pygame.display.update()

    clock.tick(60)

pygame.quit()
