import pygame.sprite

import Colors
import pygame

PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = Colors.BLACK


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image = pygame.image.load(r"C:\GitRepos\git-KourseGame\images\block.png")
        self.rect = pygame.Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)


class DieBlock(Platform):
    def __init__(self, x, y, path):
        Platform.__init__(self, x, y)
        self.image = pygame.image.load(path)

class Princes(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((21, 34))
        self.image = pygame.image.load(r"C:\GitRepos\git-KourseGame\images\Princess\princess.png")
        self.rect = pygame.Rect(x, y, 21, 34)


level1 = [
    "--------------------------------------------------",
    "-                                                -",
    "-                                                -",
    "-            *                                   -",
    "-                                ----            -",
    "-                                                -",
    "-                   ---                          -",
    "-                                                -",
    "-                                                -",
    "-                                                -",
    "-                              ----              -",
    "-                                                -",
    "-          ----                        *         -",
    "-                       -----                    -",
    "-              M                                 -",
    "-     ------------                               -",
    "-                                        P       -",
    "-                      --        *     ----      -",
    "-                           --                   -",
    "-                                                -",
    "-                                                -",
    "-------------ssss---------------------------------"]
