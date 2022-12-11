import pygame
import sys
import Colors
from ScreenSettings import gameScreen
from Player import Mario
import Levels
import Camera


def main():
    pygame.init()

    x, y = 0, 0
    mario = Mario(64, 64)
    screen = gameScreen  # переменная из файла ScreenSettings
    timer = pygame.time.Clock()

    sprites = pygame.sprite.Group()
    platforms = []
    sprites.add(mario)

    total_level_width = len(Levels.level1[0] * Levels.PLATFORM_WIDTH)
    total_level_heigth = len(Levels.level1 * Levels.PLATFORM_HEIGHT)

    camera = Camera.Camera(Camera.camera_configure, total_level_width, total_level_heigth)

    health_font = pygame.font.SysFont('Times-New-Roman', 20)
    health = pygame.image.load(r'C:\GitRepos\git-KourseGame\images\heart.png')


    for row in Levels.level1:
        for col in row:
            if col == "-":
                # создаем блок, заливаем его цветом и рисеум его
                platf = Levels.Platform(x, y)
                sprites.add(platf)
                platforms.append(platf)
            if col == "*":
                bd = Levels.DieBlock(x, y, r"C:\GitRepos\git-KourseGame\images\dieBlock.png")
                sprites.add(bd)
                platforms.append(bd)
            if col == "s":
                bd = Levels.DieBlock(x, y, r"C:\GitRepos\git-KourseGame\images\spikes.png")
                sprites.add(bd)
                platforms.append(bd)
            if col == "P":
                princess = Levels.Princes(x, y)
                sprites.add(princess)
                platforms.append(princess)
            x += Levels.PLATFORM_WIDTH
        y += Levels.PLATFORM_HEIGHT
        x = 0

    running = False

    while True:
        timer.tick(Colors.FPS)  # ограничение на количество кадров в секунду
        screen.fill(Colors.WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

        keys = pygame.key.get_pressed()
        # обработка shift - для ускоренного движения
        if keys[pygame.K_LSHIFT]:
            running = True
        if not keys[pygame.K_LSHIFT]:
            running = False

        mario.update(platforms, running)
        camera.update(mario)  # центризируем камеру относительно персонажа
        # sprites.draw(screen)  # отрисовка всего
        for e in sprites:
            screen.blit(e.image, camera.apply(e))

        health_string = f'Health: {mario.health + 1}'
        follow = health_font.render(health_string, True, Colors.BLACK)
        screen.blit(follow, (1150, 50))
        screen.blit(health, (1230, 50))
        pygame.display.update()


if __name__ == "__main__":
    main()
