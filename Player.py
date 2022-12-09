import pygame.sprite
import pyganim
import Colors

SPEED_MOVE = 7
JUMP_POWER = 10
GRAVITY = 0.35
WIDTH = 32
HEIGHT = 32

MOVE_EXTRA_SPEED = 2.5  # Укорение
JUMP_EXTRA_POWER = 1  # доп сила прыжка
ANIMATION_SUPER_SPEED_DELAY = 1  # скорость смены кадров при ускорении

# Переменные для анимации героя
CHARACTER_DELAY = 1
CHARACTER_RIGHT = ['images/Mario/r1.png',
                   'images/Mario/r2.png',
                   'images/Mario/r3.png',
                   'images/Mario/r4.png',
                   'images/Mario/r5.png']
CHARACTER_LEFT = ['images/Mario/l1.png',
                  'images/Mario/l2.png',
                  'images/Mario/l3.png',
                  'images/Mario/l4.png',
                  'images/Mario/l5.png']
CHARACTER_JUMP_LEFT = [('images/Mario/jl.png', 1)]
CHARACTER_JUMP_RIGHT = [('images/Mario/jr.png', 1)]
CHARACTER_JUMP = [('images/Mario/j.png', 1)]
CHARACTER_STOP = [('images/Mario/0.png', 1)]


class Mario(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)  # Инициализатор встроенных классов Sprite
        self.xvel = 0  # скорость перемещения по горизонтали
        self.yvel = 0  # скорость перемещения по вертикали
        self.GroundPosition = False  # на земеле или нет
        self.image = pygame.Surface((WIDTH, HEIGHT))
        self.image.fill(Colors.PURPLE)
        self.rect = pygame.Rect(x, y, WIDTH, HEIGHT)

        self.image.set_colorkey(Colors.PURPLE)  # прозрачный фон
        persAnim = []
        persAnimSuperSpeed = []
        for anim in CHARACTER_RIGHT:
            persAnim.append((anim, CHARACTER_DELAY))
            persAnimSuperSpeed.append((anim, ANIMATION_SUPER_SPEED_DELAY))
        self.persAnimRight = pyganim.PygAnimation(persAnim)
        self.persAnimRight.play()
        self.persAnimRightSuperSpeed = pyganim.PygAnimation(persAnimSuperSpeed)
        self.persAnimRightSuperSpeed.play()

        persAnim = []
        persAnimSuperSpeed = []
        for anim in CHARACTER_LEFT:
            persAnim.append((anim, CHARACTER_DELAY))
            persAnimSuperSpeed.append((anim, ANIMATION_SUPER_SPEED_DELAY))
        self.persAnimLeft = pyganim.PygAnimation(persAnim)
        self.persAnimLeft.play()
        self.persAnimLeftSuperSpeed = pyganim.PygAnimation(persAnimSuperSpeed)
        self.persAnimLeftSuperSpeed.play()

        self.persAnimStay = pyganim.PygAnimation(CHARACTER_STOP)
        self.persAnimStay.play()
        self.persAnimStay.blit(self.image, (0, 0))  # По-умолчанию, стоим

        self.persAnimJumpLeft = pyganim.PygAnimation(CHARACTER_JUMP_LEFT)
        self.persAnimJumpLeft.play()

        self.persAnimJumpRight = pyganim.PygAnimation(CHARACTER_JUMP_RIGHT)
        self.persAnimJumpRight.play()

        self.persAnimJump = pyganim.PygAnimation(CHARACTER_JUMP)
        self.persAnimJump.play()

    def update(self, platforms, running):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:  # движение влево
            self.xvel = -SPEED_MOVE
            self.image.fill(Colors.PURPLE)
            if running:
                self.xvel -= MOVE_EXTRA_SPEED
                if not keys[pygame.K_UP] or not keys[pygame.K_SPACE]:
                    self.persAnimLeftSuperSpeed.blit(self.image, (0, 0))
            else:
                if not keys[pygame.K_UP] or not keys[pygame.K_SPACE]:
                    self.persAnimLeft.blit(self.image, (0, 0))
            if keys[pygame.K_UP] or keys[pygame.K_SPACE]:
                self.persAnimJumpLeft.blit(self.image, (0, 0))

        if keys[pygame.K_RIGHT]:  # движение вправо
            self.xvel = SPEED_MOVE
            self.image.fill(Colors.PURPLE)
            if running:
                self.xvel += MOVE_EXTRA_SPEED
                if not keys[pygame.K_UP] or not keys[pygame.K_SPACE]:
                    self.persAnimRightSuperSpeed.blit(self.image, (0, 0))
            else:
                if not keys[pygame.K_UP] or not keys[pygame.K_SPACE]:
                    self.persAnimRight.blit(self.image, (0, 0))
            if keys[pygame.K_UP] or keys[pygame.K_SPACE]:
                self.persAnimJumpRight.blit(self.image, (0, 0))

        if keys[pygame.K_UP] or keys[pygame.K_SPACE]:  # прыжок
            if self.GroundPosition:
                self.yvel = -JUMP_POWER
                if running and (keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]):
                    self.yvel -= JUMP_EXTRA_POWER
            self.image.fill(Colors.PURPLE)
            self.persAnimJump.blit(self.image, (0, 0))

        if not (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]):  # стоим на месте
            self.xvel = 0
            if not (keys[pygame.K_UP] or keys[pygame.K_SPACE]):
                self.image.fill(Colors.PURPLE)
                self.persAnimStay.blit(self.image, (0, 0))

        if not self.GroundPosition:
            self.yvel += GRAVITY

        self.GroundPosition = False
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)
        self.rect.x += self.xvel
        self.collide(self.xvel, 0, platforms)

    def collide(self, xvel, yvel, platforms):
        for platf in platforms:
            if pygame.sprite.collide_rect(self, platf):  # если есть пересечение платформы с игроком
                if xvel > 0:  # если движется вправо
                    self.rect.right = platf.rect.left  # то не движется вправо

                if xvel < 0:  # если движется влево
                    self.rect.left = platf.rect.right  # то не движется влево

                if yvel > 0:  # если падает вниз
                    self.rect.bottom = platf.rect.top  # то не падает вниз
                    self.GroundPosition = True  # и становится на что-то твердое
                    self.yvel = 0  # и энергия падения пропадает

                if yvel < 0:  # если движется вверх
                    self.rect.top = platf.rect.bottom  # то не движется вверх
                    self.yvel = 0  # и энергия прыжка пропадает
