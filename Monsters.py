import pygame
import pyganim
import Colors

MONSTER_WIDTH = 32
MONSTER_HEIGHT = 32
MONSTER_COLOR = Colors.RED

ANIMATION_MONSTERHORYSONTAL = [
    (r'images/characters/fire1.png', 1),
    (r'images/characters/fire2.png', 1)
]


class Monster(pygame.sprite.Sprite):
    def __init__(self, x, y, left, maxLengthLeft):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((MONSTER_WIDTH, MONSTER_HEIGHT))
        self.image.fill(MONSTER_COLOR)
        self.rect = pygame.Rect(x, y, MONSTER_WIDTH, MONSTER_HEIGHT)
        self.image.set_colorkey(MONSTER_COLOR)
        self.startX = x
        self.startY = y
        self.maxLengthLeft = maxLengthLeft  # макс расстояние пройденное влево
        self.xvel = left  # cкорость передвижения по горизонтали, 0 - стоит на месте

        monsterAnim = []
        for anim in ANIMATION_MONSTERHORYSONTAL:
            monsterAnim.append(anim)
        self.monsterAnim = pyganim.PygAnimation(monsterAnim)
        self.monsterAnim.play()

    def update(self, platforms):
        self.image.fill(MONSTER_COLOR)
        self.monsterAnim.blit(self.image, (0, 0))

        self.rect.x += self.xvel
        self.collide(platforms)

        if abs(self.startX - self.rect.x) > self.maxLengthLeft:
            self.xvel = - self.xvel

    def collide(self, platforms):
        for platf in platforms:
            # если с чем-то столкнулись, то разворачиваемся
            if pygame.sprite.collide_rect(self, platf) and self != platf:
                self.xvel = - self.xvel
