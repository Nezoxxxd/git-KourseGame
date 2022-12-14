import pygame
import sys
import Colors
import Menu
from ScreenSettings import gameScreen
from Player import Mario
import Levels
import Camera

pygame.init()


def main():
    # pygame.init()

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
            if col == "-" or col == "_":
                # создаем блок, заливаем его цветом и рисеум его
                # choice = random.randrange(0, len(blocks_img))
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
    game_pause = False

    resume_img = pygame.image.load(r'images/buttons/resume.png').convert_alpha()
    resume_btn = Menu.Button(528, 260, resume_img)

    save_img = pygame.image.load(r'images/buttons/save.png').convert_alpha()
    save_btn = Menu.Button(528, 340, save_img)

    exit_img = pygame.image.load(r'images/buttons/exit.png').convert_alpha()
    exit_btn = Menu.Button(528, 420, exit_img)

    pause_img = pygame.image.load(r'images/backgrounds/background_pause.png').convert_alpha()
    pause_rect = pause_img.get_rect(center=(Colors.WIDTH//2, Colors.HEIGHT//2))

    while True:
        timer.tick(Colors.FPS)  # ограничение на количество кадров в секунду
        screen.fill(Colors.WHITE)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_pause = True
                    print('esc')
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
        screen.blit(follow, (1140, 50))
        screen.blit(health, (1220, 50))

        if game_pause:
            screen.blit(pause_img, pause_rect)
            if resume_btn.draw():
                game_pause = False
            if save_btn.draw():
                pass
            if exit_btn.draw():
                pygame.time.wait(100)
                Menu.menu()

        pygame.display.update()


if __name__ == "__main__":
    Menu.menu()
