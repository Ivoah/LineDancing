import pygame
import functools

import Steps
from util import *

WIDTH, HEIGHT = 50, 25

class Dancer:
    def __init__(self, couple, gender):
        self.couple = couple
        self.gender = gender
        self.pos = (couple, (0 if gender == 'F' else 1))
        self.stepf = lambda _: ((0, 0), 0)
        self.last_stepf = self.stepf
        self.progress = 0
        self.last_p = 1

        body = (255, 105, 180) if self.gender == 'F' else (0, 0, 255)
        head = tuple(c*0.5 for c in body)
        self.surf = pygame.Surface((WIDTH, HEIGHT))
        self.surf.fill((255, 255, 255))
        pygame.draw.ellipse(self.surf, body, (0, 5, WIDTH, HEIGHT - 10))
        pygame.draw.circle(self.surf, head, (WIDTH/2, HEIGHT/2), HEIGHT/2)

    def draw(self):
        return pygame.transform.rotate(self.surf, self.stepf(self.progress)[1])

    def take_step(self, step, progress):
        stepf = functools.partial(Steps.steps[step.name], self, step.meta)
        if stepf(progress):
            if progress < self.last_p:
                self.pos = add_pos(self.pos, self.last_stepf(1)[0])
                self.last_stepf = stepf
            self.stepf = stepf
            self.progress = progress
            self.last_p = progress

    def get_pos(self, root, scale):
        step_pos = self.stepf(self.progress)[0]
        return (
            root[0] + (self.pos[0] + step_pos[0])*scale[0],
            root[1] + (self.pos[1] + step_pos[1])*scale[1]
        )
