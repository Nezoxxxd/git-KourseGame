import pygame
import sys
import Colors
from ScreenSettings import gameScreen
from Player import Mario
import Levels


def main():
    pygame.init()

    x = 0
    y = 0
    # mario = Mario(64, Colors.HEIGHT - 64)
    mario = Mario(64, 64)
    screen = gameScreen
    timer = pygame.time.Clock()
    up = True

    sprites = pygame.sprite.Group()
    platforms = []
    sprites.add(mario)

    for row in Levels.level1:
        for col in row:
            if col != " ":
                # создаем блок, заливаем его цветом и рисеум его
                platf = Levels.Platform(x, y)
                sprites.add(platf)
                platforms.append(platf)
            x += Levels.PLATFORM_WIDTH
        y += Levels.PLATFORM_HEIGHT
        x = 0

    while True:
        timer.tick(Colors.FPS)  # ограничение на количество кадров в секунду
        screen.fill(Colors.WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

        mario.update(up, platforms)
        sprites.draw(screen)  # отрисовка всего

        pygame.display.update()


if __name__ == "__main__":
    main()
