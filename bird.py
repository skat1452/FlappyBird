import pygame
from pygame import *


SPEED = 0
JUMP = 10
GRAVITY = 1


class Bird(sprite.Sprite):
    def __init__(self, xpos, ypos, image):
        pygame.sprite.Sprite.__init__(self)
        self.x = xpos
        self.y = ypos
        self.yvel = 0
        self.up = False
        self.wasup = False
        self.end = False
        self.score = 0
        self.image = pygame.image.load(image)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def update(self):
        if self.up:
            self.yvel = -JUMP
            self.up = False
            self.wasup = True
        elif not self.wasup:
            self.yvel += GRAVITY
        else:
            self.wasup = False
            pygame.time.delay(20)
        self.y += self.yvel
        self.x += SPEED
        if (self.y < 0):
            self.y = 0
        if self.y >= 400:
            self.end = True
