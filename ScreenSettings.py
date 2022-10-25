import Colors
import pygame


class Screen:
    def __init__(self):
        self.gameScreen = pygame.display.set_mode((Colors.WIDTH, Colors.HEIGHT))
        pygame.display.set_caption("Mario Remaster")
        pygame.display.set_icon(pygame.image.load(r"C:\GitRepos\git-KourseGame\images\icon.png"))
