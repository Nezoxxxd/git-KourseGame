import pygame.sprite

import Colors


class Mario(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # Инициализатор встроенных классов Sprite
        self.image = pygame.Surface((50, 50))
        self.image.fill(Colors.BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (Colors.WIDTH / 2, Colors.HEIGHT / 2)


