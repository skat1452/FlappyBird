import pygame
from pygame import *
from bird import *
from block import *
from menu import *

WIN_HEIGHT = 450
WIN_WIDHT = 640


def level(window, screen):
    global best_score
    score_font = pygame.font.Font("fonts/freesansbold.ttf", 50)
    scores_screen = Surface((640, 50))
    done = True
    hero = Bird(80, 120, "bird/FlappyBird.png")
    timer = pygame.time.Clock()
    b = list()
    b_len = 4
    b_first = 0
    b.append(Block(640))
    b.append(Block(840))
    b.append(Block(1040))
    b.append(Block(1290))
    hero.up = True
    while done and not hero.end:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                done = False
            if e.type == KEYDOWN and e.key == K_SPACE:
                hero.up = True
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                done = False

        screen.fill((120, 150, 255))
        scores_screen.fill((50, 50, 50))
        hero.update()
        for b1 in b:
            b1.per(hero)
            b1.update(hero)
            b1.draw(screen)
        if b[b_first].x + 50 < 0:
            b[b_first] = Block(b[b_first - 1].x + 200)
            b_first = (b_first + 1) % b_len
        hero.draw(screen)
        scores_screen.blit(score_font.render(str(hero.score) + "  Best score: " + str(best_score), 1, (255, 255, 255)), (0, 0))
        window.blit(screen, (0, 50))
        window.blit(scores_screen, (0, 0))
        pygame.display.update()

        timer.tick(35)

    if best_score < hero.score:
        best_score = hero.score
    return done


def main():
    pygame.init()
    pygame.font.init()
    window = pygame.display.set_mode((WIN_WIDHT, WIN_HEIGHT))
    pygame.display.set_caption("Flappy bird")
    screen = Surface((WIN_WIDHT, WIN_HEIGHT))
    fin = open("score.txt", "r")
    global best_score
    for i in fin:
        best_score = int(i)
    print(best_score)
    mainmenu = Menu()
    while mainmenu.main(window, screen) and level(window, screen):
        mainmenu = Menu()
    fin.close()
    fout = open("score.txt", "w")
    fout.write(str(best_score))
    fout.close()


best_score = 0
if __name__ == "__main__":
    main()
