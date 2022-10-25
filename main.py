import pygame
import sys
import Colors
from ScreenSettings import Screen
from Player import Mario

pygame.init()

mario = Mario()
screen = Screen()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

    screen.gameScreen.fill(Colors.WHITE)
    mario.draw(screen.gameScreen)

    pygame.display.update()
