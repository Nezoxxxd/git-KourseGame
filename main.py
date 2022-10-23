import pygame
import sys
import Colors
from Player import Mario

pygame.init()

screen = pygame.display.set_mode((Colors.WIDTH, Colors.HEIGHT))
pygame.display.set_caption("Mario Remaster")
pygame.display.set_icon(pygame.image.load(r"C:\GitRepos\git-KourseGame\images\icon.png"))

all_sprites = pygame.sprite.Group()
mario = Mario()
all_sprites.add(mario)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

    screen.fill(Colors.WHITE)
    all_sprites.draw(screen)  # отрисовка персонажей из массива all_sprites

    pygame.display.update()
