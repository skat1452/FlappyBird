import pygame
import random
from pygame import *

SPEED = 7
WIDTH = 50


class Block():
    def __init__(self, x):
        self.x = x
        self.y_first = 0
        self.first_height = random.randrange(170) % 170 + 30
        self.image_first = Surface((WIDTH, self.first_height))
        self.image_first.fill((0, 0, 0))
        self.y_second = self.first_height + 150
        self.second_height = 450 - self.y_second
        self.image_second = Surface((WIDTH, self.second_height))
        self.image_second.fill((0, 0, 0))
        self.was = False

    def draw(self, screen):
            screen.blit(self.image_first, (self.x, self.y_first))
            screen.blit(self.image_second, (self.x, self.y_second))

    def update(self, bird):
        if not bird.end:
            self.x -= SPEED

    def per(self, bird):
        if (bird.x >= self.x and bird.x <= self.x + WIDTH) or (bird.x + 40 >= self.x and bird.x + 40 <= self.x + WIDTH):
            if not (bird.y > self.first_height and bird.y + 40 < self.y_second):
                bird.end = True
        if bird.x > self.x + WIDTH and not self.was:
            bird.score += 1
            self.was = True