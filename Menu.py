import sys
import pygame
import ScreenSettings

import Colors


def menu(play_btn_action):
    menu_background = pygame.Surface((Colors.WIDTH, Colors.HEIGHT))
    menu_background.fill(Colors.WHITE)

    play_button = Button(100, 50)
    exit_button = Button(100,50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(-1)

        ScreenSettings.gameScreen.blit(menu_background, (0, 0))
        play_button.draw(Colors.WIDTH / 2, Colors.HEIGHT / 2, 'Play', play_btn_action)
        exit_button.draw(Colors.WIDTH / 2, Colors.HEIGHT / 2+70, 'Exit', sys.exit)

        pygame.display.update()
        pygame.time.delay(100)


def print_text(text, x, y, font_color=Colors.BLACK, font_type='Times-New-Roman', font_size=30):
    font_type = pygame.font.SysFont(font_type, font_size)
    text = font_type.render(text, True, font_color)
    ScreenSettings.gameScreen.blit(text, (x, y))


class Button:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.inactive_clr = Colors.RED
        self.active_clr = Colors.GREEN

    def draw(self, x, y, button_text, action=None, font_size=30):
        mouse = pygame.mouse.get_pos()  # mouse[0] - координата по X, mouse[1] - координата по Y
        click = pygame.mouse.get_pressed()  # click[0] - левая кнопка мыши, click[1] - правая кнопка мыши

        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            pygame.draw.rect(ScreenSettings.gameScreen, self.active_clr, (x, y, self.width, self.height))
            if click[0] == 1:
                if action is not None:
                    action()
        else:
            pygame.draw.rect(ScreenSettings.gameScreen, self.inactive_clr, (x, y, self.width, self.height))

        print_text(button_text, x + 10, y + 10)
