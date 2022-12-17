import sys
import pygame

import Levels
import ScreenSettings
import main


def menu():
    menu_background = pygame.image.load(r'images/backgrounds/menu background.jpg')
    menu_background.blit(menu_background, (0, 0))

    start_img = pygame.image.load(r'images/buttons/start.png').convert_alpha()
    start_button = Button(512, 220, start_img)

    levels_img = pygame.image.load(r'images/buttons/levels.png').convert_alpha()
    levels_button = Button(512, 320, levels_img)

    exit_img = pygame.image.load(r'images/buttons/exit.png').convert_alpha()
    exit_button = Button(512, 420, exit_img)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(-1)

        ScreenSettings.gameScreen.blit(menu_background, (0, 0))

        if levels_button.draw():
            levels_menu()
        if start_button.draw():
            main.main()
        if exit_button.draw():
            sys.exit()

        pygame.display.update()
        pygame.time.wait(100)


def levels_menu():
    menu_background = pygame.image.load(r'images/backgrounds/menu background.jpg')
    menu_background.blit(menu_background, (0, 0))

    level1_img = pygame.image.load(r'images/buttons/level 1.png')
    level1_button = Button(512, 220, level1_img)

    level2_img = pygame.image.load(r'images/buttons/level 2.png')
    level2_button = Button(512, 320, level2_img)

    back_img = pygame.image.load(r'images/buttons/back.png').convert_alpha()
    back_button = Button(512, 420, back_img, 1.5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(-1)

        ScreenSettings.gameScreen.blit(menu_background, (0, 0))

        if level1_button.draw():
            main.level = Levels.level1
            pygame.time.wait(100)
            menu()
        if level2_button.draw():
            main.level = Levels.level2
            # pygame.time.wait(100)
            menu()
        if back_button.draw():
            pygame.time.wait(100)
            menu()

        pygame.display.update()
        pygame.time.wait(100)


class Button:
    def __init__(self, x, y, image, scale=1.5):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False
        mouse = pygame.mouse.get_pos()

        # проверка нахождения курсора на кнопке
        if self.rect.collidepoint(mouse):
            # проверка на клик левой кнопкой мыши
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked is False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        ScreenSettings.gameScreen.blit(self.image, (self.rect.x, self.rect.y))

        return action
