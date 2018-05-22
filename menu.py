import pygame
import sys
from pygame import *


class Menu():
    def __init__(self):
        self.font = pygame.font.Font(None, 32)
        self.output = ["MAIN menu", "PRESS Space to PLAY", "PRESS ESC to QUIT"]

    def main(self, window, screen):
        done = True
        progamm_done = True
        while done and progamm_done:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    progamm_done = False
                if e.type == KEYDOWN and e.key == K_SPACE:
                    done = False
                if e.type == KEYDOWN and e.key == K_ESCAPE:
                    progamm_done = False
            screen.fill((155, 200, 250))
            for i in range(len(self.output)):
                screen.blit(self.font.render(self.output[i], 1, (255, 255, 255)), (180, i * 30 + 100))

            window.blit(screen, (0, 0))
            pygame.display.update()
        return progamm_done