import pygame
import sys
import Colors

pygame.init()

screen = pygame.display.set_mode((Colors.WIDTH, Colors.HEIGHT))
pygame.display.set_caption("Mario Remaster")
pygame.display.set_icon(pygame.image.load(r"C:\GitRepos\git-KourseGame\images\icon.png"))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

    screen.fill(Colors.BLUE)
    pygame.display.update()
