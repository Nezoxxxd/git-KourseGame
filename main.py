import random
import pygame
import sys
import Colors
import Menu
from ScreenSettings import gameScreen
from Player import Mario
import Levels
import Camera
import Monsters

pygame.init()

level = Levels.level1


def main():
    x, y = 0, 0
    mario = Mario(64, 64)
    screen = gameScreen  # переменная из файла ScreenSettings
    timer = pygame.time.Clock()

    sprites = pygame.sprite.Group()
    platforms = []
    sprites.add(mario)

    monsters = pygame.sprite.Group()

    total_level_width = len(level[0] * Levels.PLATFORM_WIDTH)
    total_level_heigth = len(level * Levels.PLATFORM_HEIGHT)

    camera = Camera.Camera(Camera.camera_configure, total_level_width, total_level_heigth)

    health_font = pygame.font.SysFont('Times-New-Roman', 20)
    health = pygame.image.load(r'images/heart.png')

    for row in level:
        for col in row:
            if col == "-" or col == "_":
                # создаем блок, заливаем его цветом и рисеум его
                path = r'images/blocks/block.png'
                if col == "_":
                    path = r'images/blocks/block1.png'
                platf = Levels.Platform(x, y, path)
                sprites.add(platf)
                platforms.append(platf)
            if col == "|" or col == "=":
                # создаем блок, заливаем его цветом и рисеум его
                path = r'images/blocks/block3.png'
                if col == "=":
                    path = r'images/blocks/block2.png'
                platf = Levels.Platform(x, y, path)
                sprites.add(platf)
                platforms.append(platf)
            if col == "*":
                bd = Levels.DieBlock(x, y, r'images/blocks/dieBlock.png')
                sprites.add(bd)
                platforms.append(bd)
            if col == "s":
                bd = Levels.DieBlock(x, y, r"C:\GitRepos\git-KourseGame\images\blocks\spikes.png")
                sprites.add(bd)
                platforms.append(bd)
            if col == "P":
                princess = Levels.Princes(x, y)
                sprites.add(princess)
                platforms.append(princess)
            if col == "M":
                mn = Monsters.Monster(x, y, random.randint(0, 3), random.randint(0, 50))
                sprites.add(mn)
                platforms.append(mn)
                monsters.add(mn)

            x += Levels.PLATFORM_WIDTH
        y += Levels.PLATFORM_HEIGHT
        x = 0

    running = False
    game_pause = False

    resume_img = pygame.image.load(r'images/buttons/resume.png').convert_alpha()
    resume_btn = Menu.Button(528, 260, resume_img)

    main_menu_img = pygame.image.load(r'images/buttons/main menu.png').convert_alpha()
    main_menu_btn = Menu.Button(528, 340, main_menu_img)

    exit_img = pygame.image.load(r'images/buttons/exit.png').convert_alpha()
    exit_btn = Menu.Button(528, 420, exit_img)

    pause_img = pygame.image.load(r'images/backgrounds/background_pause.png').convert_alpha()
    pause_rect = pause_img.get_rect(center=(Colors.WIDTH // 2, Colors.HEIGHT // 2))

    while True:
        timer.tick(Colors.FPS)  # ограничение на количество кадров в секунду
        screen.fill(Colors.WHITE)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_pause = True
            if event.type == pygame.QUIT:
                sys.exit(0)

        # обработка shift - для ускоренного движения
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LSHIFT]:
            running = True
        if not keys[pygame.K_LSHIFT]:
            running = False

        mario.update(platforms, running)
        monsters.update(platforms)
        camera.update(mario)  # центризируем камеру относительно персонажа
        # sprites.draw(screen)  # отрисовка всего
        for e in sprites:
            screen.blit(e.image, camera.apply(e))

        health_string = f'Health: {mario.health + 1}'
        follow = health_font.render(health_string, True, Colors.BLACK)
        screen.blit(follow, (1140, 50))
        screen.blit(health, (1220, 50))

        if game_pause:
            screen.blit(pause_img, pause_rect)
            if resume_btn.draw():
                game_pause = False
            if main_menu_btn.draw():
                pygame.time.wait(100)
                Menu.menu()
            if exit_btn.draw():
                sys.exit(0)

        pygame.display.update()


if __name__ == "__main__":
    Menu.menu()
