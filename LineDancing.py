#!/usr/bin/env python3
import pygame

from pygame.locals import *

from Dancer import Dancer
from Dance import Dance

WIDTH, HEIGHT = 640, 480
NUM_DANCERS = 8
SCALE = (100, 150)
ROOT = (
    (WIDTH - (NUM_DANCERS/2 - 1)*SCALE[0])/2,
    (HEIGHT - (2 - 1)*SCALE[1])/2
)

pygame.init()

pygame.display.set_caption('Line Dancing', 'Line Dancing')
window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
clock = pygame.time.Clock()
font = pygame.font.SysFont('Helvetica', 24)

dancers = [Dancer(i//2, 'F' if i%2 else 'M') for i in range(NUM_DANCERS)]
dance = Dance('Hole in the Wall')

pygame.mixer.music.load(dance.song)
pygame.mixer.music.play()
playing = True

running = True
while running:
    for event in pygame.event.get():
        if (event.type == KEYDOWN and event.mod == 1024 and event.key == 113) or event.type == QUIT:
            running = False
        elif event.type == KEYDOWN and event.key == K_SPACE:
            if playing:
                pygame.mixer.music.pause()
            else:
                pygame.mixer.music.unpause()
            playing = not playing

    window.fill((255, 255, 255))

    for i, step in enumerate(dance.get_steps(pygame.mixer.music.get_pos())):
        window.blit(font.render(f'{step[0].name} {step[1]*100:.2f}%', True, (0, 0, 0)), (20, 20*(i + 1)))
        for dancer in dancers:
            dancer.take_step(*step)
    
    window.blits(list((dancer.draw(), dancer.draw().get_rect(center=dancer.get_pos(ROOT, SCALE))) for dancer in dancers))

    pygame.display.flip()
    clock.tick(60)
