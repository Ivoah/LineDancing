import pygame

from pygame.locals import *

pygame.init()

WIDTH, HEIGHT = 640, 480
window = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.SysFont('Helvetica', 24)

pygame.mixer.music.load('Songs/Hole in the Wall.ogg')
pygame.mixer.music.play()

paused = False
running = True
while running:
    for event in pygame.event.get():
        if (event.type == KEYDOWN and event.mod == 1024 and event.key == 113) or event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                if paused:
                    pygame.mixer.music.unpause()
                    paused = False
                else:
                    pygame.mixer.music.pause()
                    paused = True
            elif event.key == K_LEFT:
                pygame.mixer.music.play()

    window.fill((0, 255, 255))
    window.blit(font.render(str(pygame.mixer.music.get_pos()), True, (0, 0, 0)), (10, 10))
    pygame.display.flip()
