import pygame
import sys
import Colors
import Menu
from ScreenSettings import gameScreen
from Player import Mario
import Levels
import Camera

pygame.init()

level = Levels.level1
menu_sound = pygame.mixer.Sound(r"music/Menu music.wav")
menu_sound.set_volume(0.4)
pygame.mixer.music.load(r'music/mouse_click.mp3')
pygame.mixer.music.set_volume(1)


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

    # функция генерации уровня
    Levels.level_create(level, x, y, platforms, sprites, monsters)

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

    # bg = pygame.image.load(r'images/backgrounds/level_background.jpg')

    Menu.menu_sound.stop()
    menu_sound.play()

    while True:
        timer.tick(Colors.FPS)  # ограничение на количество кадров в секунду
        screen.fill(Colors.SKY)
        # screen.blit(bg, (0, 0))

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
                menu_sound.stop()
                Menu.menu()
            if exit_btn.draw():
                sys.exit(0)

        pygame.display.update()


if __name__ == "__main__":
    Menu.menu()
