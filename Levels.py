import pygame.sprite
import Colors
import pygame
import random
import Monsters

PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = Colors.BLACK


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image = pygame.image.load(image_path)
        self.rect = pygame.Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)


class DieBlock(Platform):
    def __init__(self, x, y, path):
        Platform.__init__(self, x, y, path)
        self.image = pygame.image.load(path)


class Princes(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((21, 34))
        self.image = pygame.image.load(r"images/characters/princess.png")
        self.rect = pygame.Rect(x, y, 21, 34)


def level_create(level, x, y, platforms, sprites, monsters):
    for row in level:
        for col in row:
            if col == "-" or col == "_" or col == '~':
                # создаем блок, заливаем его цветом и рисеум его
                path = r'images/blocks/block.png'
                if col == "_":
                    path = r'images/blocks/block1.png'
                if col == "~":
                    path = r'images/blocks/block4.png'
                platf = Platform(x, y, path)
                sprites.add(platf)
                platforms.append(platf)
            if col == "|" or col == "=":
                # создаем блок, заливаем его цветом и рисеум его
                path = r'images/blocks/block3.png'
                if col == "=":
                    path = r'images/blocks/block2.png'
                platf = Platform(x, y, path)
                sprites.add(platf)
                platforms.append(platf)
            if col == "*":
                bd = DieBlock(x, y, r'images/blocks/dieBlock.png')
                sprites.add(bd)
                platforms.append(bd)
            if col == "s":
                bd = DieBlock(x, y, r"C:\GitRepos\git-KourseGame\images\blocks\spikes.png")
                sprites.add(bd)
                platforms.append(bd)
            if col == "P":
                princess = Princes(x, y)
                sprites.add(princess)
                platforms.append(princess)
            if col == "M":
                mn = Monsters.Monster(x, y, random.randint(0, 3), random.randint(0, 70))
                sprites.add(mn)
                platforms.append(mn)
                monsters.add(mn)

            x += PLATFORM_WIDTH
        y += PLATFORM_HEIGHT
        x = 0


level1 = [
    "-----------------------------------------------------------------------------------------------------------------",
    "-                                             -                                                                 -",
    "-                                           P -                                                                 -",
    "-                                     ---------                                                                 -",
    "-                                                                                                               -",
    "-                           ---                                                                                 -",
    "-                                               ------                                                          -",
    "-                                                                                                               -",
    "-                                                                                                               -",
    "-                                                            ----                                               -",
    "-                                                                   **     -----                                -",
    "-                                                                                                               -",
    "-                                                                                                               -",
    "-                                      ----                                                                     -",
    "-                                                                           *     --                            -",
    "-                        s                    **           ---                                                  -",
    "-                        =                                             -----               -----                -",
    "-                       *|                                                                                    ---",
    "-                       *|                               =                                                      -",
    "-                       *|                             = |                                                      -",
    "-                       *|                           = | |                                                      -",
    "-            ssss       *|        M                =s|s|s|ssssssssss                                            -",
    "-_____________________  _______________________________________________________________________    _____________-",
    "-                        ~                      -                                             ~    ~            -",
    "-    ~~~~~~~~~~~~~~~~~~~~~                                                                    ~    ~            -",
    "-                                       ~~~   ___________s___s___s____                        ~~   ~            -",
    "-                                  =            ~~~~~~~~~~~~~~~~~~~~~     =                   ~   ~~            -",
    "-ssss             M                |ssssssssssss~~~~~~~~~~~~~~~~~~~~~sssss|          M             ~            -",
    "-_______________________________________________________________________________________________________________-"]

level2 = [
    "---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "-                                                                                                                       -       *                -         -                                            -",
    "-                                                                                                                       -               ---                                                             -",
    "-                                                                                                                       -    s      M                                                                   -",
    "-                                                                                                                       ---  -------------------------------                                            -",
    "-                                                                                                                       -                                  -                                            -",
    "-                                                                                                                       ------------------------------     -                                            -",
    "-                                                                                                                       -                             --   -                                            -",
    "-                                                                                                                     * -                                  -                                            -",
    "-          -----------                                      --                                                        * -        --        ---            --                                          ---",
    "-                                                                                                                               M       ssss      M        -                                            -",
    "-                                             -----                                                                     ------------------------------------                                           P-",
    "-                                                                                  ---                                                                                                                ---",
    "-                                  ---                 ***       M                                    ----                                                                                              -",
    "-                                                             ------                                                                                                                         =          -",
    "-                                                                                                                                                                                            |          -",
    "-                                       *   -                                                    ---                                                                                         |          -",
    "-                        =      -----                                                                                                                                              =         |          -",
    "-                  =     |                                                                           *                                                                             |         |          -",
    "-                  |     |                                                                       ---                                                                      =        |         |          -",
    "-              =   |     |                                                                                                                                                |        |         |          -",
    "-              |   |     |                                                       M           **                                                                           |        |         |          -",
    "-_______________sss_sssss__ssssssssssssssssssssssssssssssssssssssssssss___________________________sssssssssssssssssssssssssssssssssss______________________________________ssssssss_ssssssss___sssssss__-"]
